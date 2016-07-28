from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    phone = models.CharField(
            max_length=20,
            null=True,
            blank=True,
            )
