from django.db import models
from django.conf import settings
from django.utils import timezone


def localtime():
    return timezone.localtime(timezone.now())


class ItemPost(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            )

    # it will used item admin
    def user_nickname_def(self):
        return self.user.nickname

    user_nickname = property(user_nickname_def)

    title = models.TextField(
            )

    created_at = models.DateTimeField(
            default=localtime
            )

    updated_at = models.DateTimeField(
            default=localtime,
            )

    is_deleted = models.BooleanField(
            default=False,
            verbose_name="삭제된 포스트",
            )

    # 마감날짜를 구하는 함수
    def deadline_def(self):
        year_of_item_created = self.created_at.year

        if self.created_at.month <= 6:
            return timezone.datetime(year_of_item_created, 6, 30, tzinfo=timezone.utc)
        else:
            return timezone.datetime(year_of_item_created, 12, 31, tzinfo=timezone.utc)

    deadline = property(deadline_def)

    # 등록된 학기가 끝난 포스트인지 확인
    def is_ended_semester_def(self):
        now = timezone.now()
        if now > self.deadline:
            return True
        return False

    is_ended_semester = property(is_ended_semester_def)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = verbose_name
