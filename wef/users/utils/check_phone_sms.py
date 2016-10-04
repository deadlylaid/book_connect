import os
import requests


class SendPhoneCheckSMS():

    def send_sms(self, phone_number, token):
        API_BASE_URL = os.environ.get("API_BASE_URL")
        response = requests.post(
                API_BASE_URL,
                data={
                    'send_phone': '01020370706',
                    'dest_phone': phone_number,
                    'msg_body': '회원님의 인증번호는 ['+token+'] 입니다',
                    },
                headers={
                    "x-waple-authorization": os.environ.get("SMS_AUTHORIZATION")
                    },
                )

        return response
