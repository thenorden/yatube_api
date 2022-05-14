from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets, status
from rest_framework import filters
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from posts.models import Post, Comment, Group, User, Follow
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_queryset(self):
        queryset = Post.objects.select_related('group')
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group__slug=group)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Group.objects.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('user__username', 'author__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        queryset = Follow.objects.filter(author=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
