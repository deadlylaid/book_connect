from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from django.http import HttpRequest

from wef.views import Home

from users.views import join_us
from users.models import User


class HomePageTest(TestCase):

    # home화면에 들어가면 home view를 호출한다.
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__, Home.__name__)

    # home url을 입력하면 home.html을 랜더링한다.
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class UserTest(TestCase):

    def setUp(self):
        self.username = 'test_user'
        self.password = 'password'
        self.phone = '01022222222'
        self.user = User.objects.create_user(username=self.username, password=self.password, phone=self.phone)

    # joinus url에 들어가면 join_us view를 호출한다.
    def test_join_us_url_resolve_to_join_us_view(self):
        found = resolve('/joinus/')
        self.assertEqual(found.func, join_us)

        response = self.client.get('/joinus/')
        self.assertTemplateUsed(response, 'users/joinus.html')

    # User모델은 새로 회원가입한 유저 데이터를 저장할 수 있다.
    # Username 중복체크는 django에 자동 구현되어있기 때문에
    # 테스트 하지 않는다.
    def test_user_log_in(self):

        response = self.client.login(username=self.username, password=self.password)
        self.assertTrue(response)

    # 비밀번호를 바꿔서 로그인
    # 로그인에 실패하는 것을 확인하고 비밀번호 변경
    def test_user_password_reset(self):

        self.password = 'reset_password'
        response = self.client.login(username=self.username, password=self.password)
        self.assertFalse(response)

#        send_reset_password_post = self.client.put(
#                '/password/reset/',
#                {'username': 'test_user', 'password': self.password}
#                )
#        self.assertEqual(send_reset_password_post.status_code, 302)
#
#        response = self.client.login(username=self.username, password=self.password)
#        self.assertTrue(response)
