from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User


class CheckToken(APIView):

    def put(self, request, *args, **kwargs):

        received_token = request.data.get('token_num')
        response_data = {}

        if request.user.certification_code == received_token:
            request.user.passed_certification = True
            request.user.save()
            response_data['certification'] = True

            return Response(response_data, status=status.HTTP_200_OK)

        else:
            response_data['certification'] = False
            return Response(response_data, status=status.HTTP_200_OK)
