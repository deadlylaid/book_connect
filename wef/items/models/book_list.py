from django.db import models
from .item_post import ItemPost


class BookList(models.Model):
    # post + booknumber => primarykey로 쓰인다

    post = models.ForeignKey(
            "ItemPost",
            )

    booknumber = models.IntegerField(
            )

    bookname = models.CharField(
            max_length=200,
            )

    bookprice = models.CharField(
            max_length=200,
            )

    price_undefined = models.BooleanField(
            default=False,
            )

    is_soldout = models.BooleanField(
            default=False,
            )

    def __str__(self):
        return self.bookname
