import os
import requests


class SendSMS():

    def send_sms(self, buyer_nickname, buyer_phone, saler_phone, selected_bookname):
        API_BASE_URL = os.environ.get("API_BASE_URL")
        response = requests.post(
                API_BASE_URL,
                data={
                    'send_phone': '01020370706',
                    'dest_phone': saler_phone,
                    'msg_body': buyer_nickname+' 님께서 회원님의 ' +
                    selected_bookname + '를 구매하고 싶어하십니다. 구매자 전화번호:' + buyer_phone,
                    },
                headers={
                    "x-waple-authorization": os.environ.get("SMS_AUTHORIZATION")
                    },
                )

        return response
