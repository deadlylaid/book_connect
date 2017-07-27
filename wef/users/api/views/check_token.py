from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User


class CheckToken(APIView):

    def put(self, request, *args, **kwargs):

        received_token = request.data.get('token_num')
        response_data = {}

        if not request.user.is_anonymous():
            if request.user.certification_code == received_token:
                request.user.passed_certification = True
                request.user.save()
                response_data['certification'] = True

                return Response(response_data, status=status.HTTP_200_OK)

            else:
                response_data['certification'] = False
                return Response(response_data, status=status.HTTP_200_OK)
        else:
            received_phone_number = request.data.get('phone_number')

            searched_user_by_phone_number = User.objects.get(phone=received_phone_number)

            if searched_user_by_phone_number.certification_code == received_token:
                searched_user_by_phone_number.passed_certification = True
                searched_user_by_phone_number.save()
                response_data['certification'] = True
                response_data['username'] = searched_user_by_phone_number.username

                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data['certification'] = False
                return Response(response_data, status=status.HTTP_200_OK)
