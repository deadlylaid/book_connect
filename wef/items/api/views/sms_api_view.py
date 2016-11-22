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

        # 로그인이 되어있는 상태라면 문자를 보낸다
        if request.user.is_authenticated():

            buyer_nickname = request.user.nickname
            buyer_phone = request.user.phone

            if buyer_phone:
                selected_bookname = request.data.get('bookname')

                sms = SendBuyMessageTask()
                sms.delay(buyer_nickname, buyer_phone, saler_phone, selected_bookname)

                response_data = {}
                response_data['send'] = True
                return Response(response_data, status=status.HTTP_200_OK)

            response_data = {}
            response_data['send'] = False
            return Response(response_data, status=status.HTTP_200_OK)

        # 로그인이 되어있지 않으면 문자를 보내지 않는다
        response_data = {}
        response_data['send'] = False
        return Response(response_data, status=status.HTTP_200_OK)
