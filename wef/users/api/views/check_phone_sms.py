from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.utils import maketoken
from users.tasks import SendPhoneCheckSMSTask


class PhoneNumberCheck(APIView):

    def post(self, request, *args, **kwargs):
        received_phone_number = request.data.get('phone_number')

        overlap_phone_number_user = User.objects.filter(
                phone=received_phone_number,
                )

        response_data = {}

        if request.user.is_anonymous():
            '''
            ID, password search
            '''
            try:
                searched_user_by_phone_number = overlap_phone_number_user[0]
            except IndexError as e:
                # 일치하는 회원정보 없음
                #status는 추후 변경
                response_data['result'] = False
                response_data['id'] = None
                return Response(response_data, status=status.HTTP_200_OK)

            # 일치하는 회원정보 있음
            response_data['result'] = True
            response_data['id'] = searched_user_by_phone_number.username
            return Response(response_data, status=status.HTTP_200_OK)

        else:
            '''
            join us
            '''
            if overlap_phone_number_user:
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
