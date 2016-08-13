from django.db import models
from django.conf import settings


class ItemPost(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            )

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
