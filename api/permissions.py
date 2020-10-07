from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import mixins, viewsets


class OnlyCreatorPermission(BasePermission):
    massage = "Нет прав на данное действие"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author


class BaseCreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass
