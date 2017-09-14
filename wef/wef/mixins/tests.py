from django.test import TestCase

from users.models import User


class SetUpMixin(TestCase):

    def setUp(self):
        self.username = 'test_user'
        self.password = 'password'
        self.phone = '01022222222'
        self.user = User.objects.create_user(username=self.username, phone=self.phone)
        self.user.set_password(self.password)
        self.user.save()


class SetUpLogInMixin(SetUpMixin):

    def setUp(self):
        SetUpMixin.setUp(self)
        self.client.login(username=self.username, password=self.password)
