from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from wef.views import home

from users.views import join_us
from users.models import User


class HomePageTest(TestCase):

    # home화면에 들어가면 home view를 호출한다.
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__, home.__name__)

    # home url을 입력하면 home.html을 랜더링한다.
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class UserTest(TestCase):

    # joinus url에 들어가면 join_us view를 호출한다.
    def test_join_us_url_resolve_to_join_us_view(self):
        found = resolve('/joinus/')
        self.assertEqual(found.func, join_us)

        response = self.client.get('/joinus/')
        self.assertTemplateUsed(response, 'users/joinus.html')

    # User모델은 새로 회원가입한 유저 데이터를 저장할 수 있다.
    # Username 중복체크는 django에 자동 구현되어있기 때문에
    # 테스트 하지 않는다.
    def test_User_model_can_save_user_data(self):

        user = User.objects.create_user(username='testID', password='123', phone='', email='')
        user.save()

        self.assertEqual(User.objects.first().username, 'testID')
