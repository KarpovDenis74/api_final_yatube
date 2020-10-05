from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework import mixins, viewsets


class OnlyCreatorPermission(BasePermission):
    massage = "Нет прав на данное действие"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return True
    #     return False



class BaseCreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass