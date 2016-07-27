from django.core.urlresolvers import resolve
from django.test import TestCase
from users.views import join_us


class HomePageTest(TestCase):

    # home화면에 들어가자마자 회원가입을 유도하는 페이지 호출
    # 차후 리펙토링 예정
    def test_root_rul_resolves_to_Join_Us_view(self):
        found = resolve('/')
        self.assertEqual(found.func, join_us)
