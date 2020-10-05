# TODO:  Напишите свой вариант
from .models import Post, Comment, Group, Follow, User
from .serializers import (PostSerializer, CommentSerializer,
    GroupSerializer, FollowSerializer)
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .permissions import OnlyCreatorPermission, BaseCreateListViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .filters import FollowFilter, PostFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OnlyCreatorPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group=group)
            return queryset
        return Post.objects.all()



class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [OnlyCreatorPermission]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(BaseCreateListViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     title = self.request.query_params.get('title', None)
    #     serializer.save(title=title)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.query_params.post('follow'),
    #         author=self.request.query_params.post('following'))

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.request.query_params.get('search'))
    #     print(user)
    #     if user is not None:
    #         follow = get_object_or_404(Follow, user=user)
    #         return follow
    #     return Follow.objects.all()
