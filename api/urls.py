from django.urls import path, include
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView
    )
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='api_posts')
router.register(r'posts',
    PostViewSet, basename='api_comments')
router.register(r'group',
    GroupViewSet, basename='api_groups')
router.register(r'follow',
    FollowViewSet, basename='api_follow')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    ]
