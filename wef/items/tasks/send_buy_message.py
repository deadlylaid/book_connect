from celery import Task

from items.utils import SendSMS


class SendBuyMessageTask(Task):

    def run(self, buyer_nickname, buyer_phone, saler_phone, selected_bookname):
        sms = SendSMS()
        sms.send_sms(buyer_nickname, buyer_phone, saler_phone, selected_bookname)
        print("Task success")
