from django.db import models
from django.conf import settings
from django.utils import timezone


def localtime():
    return timezone.localtime(timezone.now())


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
            default=localtime
            )

    updated_at = models.DateTimeField(
            default=localtime,
            )

    is_deleted = models.BooleanField(
            default=False,
            )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = verbose_name
