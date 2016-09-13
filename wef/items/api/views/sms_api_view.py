from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from items.models import BookList, ItemPost
from items.api.serializers import BookListSerializer
from items.tasks.send_buy_message import SendBuyMessageTask

import os


class SendBuySMSAPIView(APIView):

    def post(self, request, *args, **kwargs):

        sms = SendBuyMessageTask()
        sms.delay()

        return Response(status=status.HTTP_204_NO_CONTENT)
