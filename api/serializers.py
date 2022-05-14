from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer. Mandatory field "author".
    """
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer. Mandatory field "author".
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """
    Follow serializer. Checks the request method and occurrence of errors.
    Has unique fields.
    """
    user = serializers.SlugRelatedField(slug_field='username', read_only=True, default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    def validate_following(self, following):
        if self.context.get('request').method == 'POST':
            if following is None:
                raise serializers.ValidationError('Request missing a field following')
            if self.context.get('request').user == following:
                raise serializers.ValidationError('You cant subscribe to yourself')
        return following

    class Meta:
        fields = '__all__'
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    """
    Group serializer.
    """

    class Meta:
        fields = '__all__'
        model = Group
