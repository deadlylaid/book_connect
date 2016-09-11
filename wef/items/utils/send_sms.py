import os
import requests

API_BASE_URL = os.environ.get("API_BASE_URL")

response = requests.post(
        API_BASE_URL,
        data={
            'send_phone': '01020370706',
            'dest_phone': '01020370706',
            'msg_body': 'TEST',
            },
        headers={
            "x-waple-authorization": os.environ.get("SMS_AUTHORIZATION")
            }
        )

print(response.status_code, response.content)
