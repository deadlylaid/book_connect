from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from users.models import User


class CheckOverlapUsername(APIView):

    def post(self, request, *args, **kwargs):
        received_username = request.data.get('received_username')

        overlap_id = User.objects.filter(
                username=received_username,
                )

        response_data = {}

        if overlap_id:
            response_data['overlap'] = True
        else:
            response_data['overlap'] = False

        return Response(
                response_data,
                status=status.HTTP_200_OK)
