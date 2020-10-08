from .models import Post, Follow, Group
from django_filters import rest_framework as filters


class PostFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name="pub_date",
                                       lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name="pub_date", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['date_from', 'date_to']


class FollowFilter(filters.FilterSet):

    class Meta:
        model = Follow
        fields = '__all__'


class PostFilter(filters.FilterSet):

    class Meta:
        model = Group
        fields = ['slug']
