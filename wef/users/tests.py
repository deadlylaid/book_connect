from django.core.urlresolvers import resolve
from django.test import TestCase
from users.views import join_us


class HomePageTest(TestCase):

    def test_root_rul_resolves_to_Join_Us_view(self):
        found = resolve('/')
        self.assertEqual(found.func, join_us)
