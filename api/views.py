from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


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



