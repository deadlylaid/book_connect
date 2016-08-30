from rest_framework import serializers
from items.models import BookList


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookList
        fields = (
                'bookname',
                'bookprice',
                'is_soldout',
                )
