from rest_framework import serializers

from posts.models import Post, Comment, User


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'username')
#         model = User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = instance.author.username
        if representation["group"]:
            representation["group"] = instance.group.slug
        return representation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']
