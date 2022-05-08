from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# class PostCreateAPIView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#
# class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CommentsCreateAPIView(ListCreateAPIView):
#     queryset = Comment.objects.all(post__pk=id)
#     serializer_class = CommentSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        comments = post.comments.all()
        return comments




# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#     def get_queryset(self):
#         post = get_object_or_404(Post, pk=self.kwargs['post_id'])
#         return post.comments.all()

