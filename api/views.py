from .models import Post, Group, Follow
from .serializers import (PostSerializer, CommentSerializer,
    GroupSerializer, FollowSerializer)
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .permissions import OnlyCreatorPermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters, mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend



class BaseCreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OnlyCreatorPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'group']


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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


class FollowViewSet(BaseCreateListViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
