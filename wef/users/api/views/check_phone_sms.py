from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.utils import maketoken
from users.tasks import SendPhoneCheckSMSTask


class PhoneNumberCheck(APIView):

    def post(self, request, *args, **kwargs):
        received_phone_number = request.data.get('phone_number')

        overlap_phone_number = User.objects.filter(
                phone=received_phone_number,
                )

        response_data = {}

        if overlap_phone_number:
            response_data['sms'] = False
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data['sms'] = True
            token = str(maketoken())

            # 생성된 코드를 user model의 column에 넣는다.
            request.user.certification_code = token
            request.user.save()

            task = SendPhoneCheckSMSTask()
            task.delay(received_phone_number, token)

            return Response(response_data, status=status.HTTP_200_OK)
