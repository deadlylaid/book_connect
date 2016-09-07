from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from items.models import BookList, ItemPost
from items.api.serializers import BookListSerializer


class BookListAPIView(APIView):

    def put(self, request, *args, **kwargs):

        post_id = request.data.get('post_id')
        book_list_id = request.data.get('book_list_id')

        itempost = ItemPost.objects.get(pk=post_id)

        if request.user.username == itempost.user.username:
            getted_book_list = BookList.objects.get(
                   post=itempost,
                   booknumber=book_list_id,
                   )

            if not getted_book_list.is_soldout:
                getted_book_list.is_soldout = True
                getted_book_list.save()

                serializer = BookListSerializer(getted_book_list)
                if BookListSerializer(data=serializer.data):
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            getted_book_list.is_soldout = False
            getted_book_list.save()

            serializer = BookListSerializer(getted_book_list)
            if BookListSerializer(data=serializer.data):
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
