import os
import requests
import json


class SendSMS():

    def send_sms(self, buyer_nickname, buyer_phone, saler_phone, selected_bookname):
        appid = os.environ.get("APPID")
        apikey = os.environ.get("APIKEY")

        sender = '01020370706'
        receivers = [saler_phone, ]

        content = u'[북커넥트]'+ selected_bookname + ' 판매요청. 요청자 번호:'+ buyer_phone

        url = os.environ.get("URL")

        params = {
                'sender': sender,
                'receivers': receivers,
                'content': content,
        }
        headers = {'Content-type': 'application/json; charset=utf-8', }
        r = requests.post(url, data=json.dumps(params), auth=(appid, apikey), headers=headers)

        return params
