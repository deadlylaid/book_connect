from celery import Task

from users.utils import SendPhoneCheckSMS


class SendPhoneCheckSMSTask(Task):

    def run(self, phone_number, token):
        sms = SendPhoneCheckSMS()
        sms.send_sms(phone_number, token)
        print("Task success")
