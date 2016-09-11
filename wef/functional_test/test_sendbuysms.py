from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from users.models import User
from items.models import ItemPost, BookList


class OurClientCanSendSMSIfBuyBook(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        user1 = User.objects.create_user(
                username='MyTestID',
                password='123',
                nickname='NICKNAMETEST',
                phone='01011111111')
        itempost = ItemPost.objects.create(user=user1, title='posttitle')
        booklist1 = BookList.objects.create(post=itempost, booknumber=1, bookname='book1', bookprice='1000')
        user2 = User.objects.create_user(
                username='MyTestID2',
                password='123',
                nickname='NICKNAMETEST2',
                phone='01011111111')

    def tearDown(self):
        self.browser.quit()

    def test_our_client_can_log_in_and_send_sms(self):

        # 민수는 중고 도서공유 사이트에 url접속을 한다.
        self.browser.get(self.live_server_url)

        # 웹 페이지는 헤더가 '남서울 도서공유'를 표시하고 있다.
        self.assertIn('남서울 도서공유', self.browser.title)

        # 메인 페이지에 있는 로그인 버튼을 클릭한다.
        log_in = self.browser.find_element_by_id('log_in')
        log_in.send_keys(Keys.ENTER)
        self.assertIn('로그인', self.browser.title)

        # 로그인 페이지에서 아이디와 비빌번호를 입력하고
        # 확인 버튼을 누른다
        username_box = self.browser.find_element_by_name('username')
        password_box = self.browser.find_element_by_name('password')

        username_box.send_keys('MyTestID2')
        password_box.send_keys('123')

        self.browser.find_element_by_id('button').click()
        self.assertIn('남서울 도서공유', self.browser.title)
        # 포스트링크에 들어간다.
        self.browser.get('http://localhost:8000/booksale/1/')

        # 마음에 드는 중고책이 있어서 판매자에게 문자를 보낸다
        self.browser.find_element_by_id('msg1').click()
        # 문자가 보내지기 전에 알림창으로 휴대폰번호 제공 공지가 뜬다
        # 확인버튼을 누르면 문자가 날아간다.
