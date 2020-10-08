from django.urls import path, include
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView
    )
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='api_posts')
router.register(r'v1/posts',
    PostViewSet, basename='api_comments')
router.register(r'v1/group',
    GroupViewSet, basename='api_groups')
router.register(r'v1/follow',
    FollowViewSet, basename='api_follow')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    ]
