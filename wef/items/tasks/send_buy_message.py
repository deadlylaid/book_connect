from celery import Task

from items.utils import SendSMS


class SendBuyMessageTask(Task):

    def run(self):
        sms = SendSMS()
        sms.send_sms()
        print("Task success")
