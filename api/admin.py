from django.contrib import admin
from .models import Post, Group, Comment, Follow


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    search_fields = ("title",)
    list_filter = ("slug",)
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "author", "text", "created",)
    search_fields = ("text",)
    list_filter = ("created",)


class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "following",)
    search_fields = ("user",)
    list_filter = ("following",)


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)