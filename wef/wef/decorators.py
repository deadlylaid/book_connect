from django.utils import timezone

import logging


def log_decorator(func):

    logger = logging.getLogger(__name__)

    def wrap_func(self, *args, **kwargs):

        # buyer_nickname, buyer_phone, saler_phone, selected_bookname
        # 순서로 리스트에 담김
        # 이 데이터들은 로그를 출력하는데 이용될 것이다.
        list_of_user_data = args

        time_stamp = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
        logger.info('[{}] 도서제목 : {} //  발신자 : {} // 수신자 : {}'.format(
            time_stamp,
            list_of_user_data[3],
            list_of_user_data[1],
            list_of_user_data[2]
            )
        )
        return func(self, *args, **kwargs)
    return wrap_func
