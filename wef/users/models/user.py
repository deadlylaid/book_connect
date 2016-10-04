from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    nickname = models.CharField(
            max_length=20,
            null=True,
            blank=True,
            )

    phone = models.CharField(
            max_length=20,
            null=True,
            blank=True,
            )

    certification_code = models.CharField(
            max_length=4,
            null=True,
            blank=True,
            )

    passed_certification = models.BooleanField(
            default=False,
            )

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = verbose_name
