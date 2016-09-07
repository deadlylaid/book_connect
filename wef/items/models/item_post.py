from django.db import models
from django.conf import settings


class ItemPost(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            )

    # it will used item admin
    def user_nickname_def(self):
        return self.user.nickname

    user_nickname = property(user_nickname_def)

    title = models.TextField(
            )

    created_at = models.DateTimeField(
            auto_now_add=True,
            )

    updated_at = models.DateTimeField(
            auto_now=True,
            )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = verbose_name
