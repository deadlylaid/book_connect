from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from wef.views import home
from users.views import join_us


class HomePageTest(TestCase):

    # home화면에 들어가면 home view를 호출한다.
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    # home url을 입력하면 home.html을 랜더링한다.
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class UserTest(TestCase):

    # joinus url에 들어가면 join_us view를 호출한다.
    def test_join_us_url_resolve_to_join_us_view(self):
        found = resolve('/joinus/')
        self.assertEqual(found.func, join_us)

    # joinus form에서 데이터를 입력해서 submit을 하면
    # joinus view로 데이터를 보낸다
    def test_join_us_form_send_data_to_join_us_view(self):
        found = resolve('/joinus/')
        self.assertEqual(found.func, join_us)
