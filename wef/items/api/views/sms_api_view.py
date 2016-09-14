from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from items.models.item_post import ItemPost
from items.tasks.send_buy_message import SendBuyMessageTask

import os


class SendBuySMSAPIView(APIView):

    def post(self, request, *args, **kwargs):

        post_id = request.data.get('post_id')

        itempost = ItemPost.objects.get(pk=post_id)
        saler_phone = itempost.user.phone

        buyer_nickname = request.user.nickname
        buyer_phone = request.user.phone
        selected_bookname = request.data.get('bookname')

        sms = SendBuyMessageTask()
        sms.delay(buyer_nickname, buyer_phone, saler_phone, selected_bookname)

        return Response(status=status.HTTP_204_NO_CONTENT)
