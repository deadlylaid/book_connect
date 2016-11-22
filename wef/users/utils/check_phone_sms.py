import os
import requests
import json


class SendPhoneCheckSMS():

    def send_sms(self, phone_number, token):
        appid = os.environ.get("APPID")
        apikey = os.environ.get("APIKEY")

        sender = '01020370706'
        receivers = [phone_number, ]

        content = u'회원님의 인증번호는 ['+token+']입니다.'

        url = os.environ.get("URL")

        params = {
                'sender': sender,
                'receivers': receivers,
                'content': content,
        }
        headers = {'Content-type': 'application/json; charset=utf-8', }
        r = requests.post(url, data=json.dumps(params), auth=(appid, apikey), headers=headers)

        return params
