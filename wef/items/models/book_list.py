from django.db import models
from .item_post import ItemPost


class BookList(models.Model):

    post = models.ForeignKey(
            "ItemPost",
            )

    bookname = models.CharField(
            max_length=200,
            )

    bookprice = models.CharField(
            max_length=200,
            )

    is_soldout = models.BooleanField(
            default=False,
            )
