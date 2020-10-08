from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name="Название сообщества",
        max_length=200)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст поста",
        )
    pub_date = models.DateTimeField("date published",
                                    auto_now_add=True,
                                    db_index=True
                                    )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              related_name="group",
                              blank=True,
                              null=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    post = models.ForeignKey(Post,
                            on_delete=models.CASCADE,
                            related_name="comments"
                            )
    author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="comments"
                            )
    text = models.TextField(
        verbose_name="Текст комментария",
    )
    created = models.DateTimeField("date created",
                            auto_now_add=True,
                            db_index=True
                            )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']


class Follow(models.Model):
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="follower"
                            )
    following = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="following"
                            )

    class Meta:
        unique_together = ("user", "following")
