from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_sign_up_and_log_in_out_this_website(self):

        # 민수는 중고 도서공유 사이트가 있다는 소릴듣고 url접속을 한다.
        self.browser.get(self.live_server_url)

        # 웹 페이지는 헤더가 '남서울 도서공유'를 표시하고 있다.
        self.assertIn('남서울 도서공유', self.browser.title)

        # 민수는 회원가입을 하고싶다.
        # 민수는 회원가입 버튼을 누른다.
        join_us = self.browser.find_element_by_id('join_us')
        join_us.send_keys(Keys.ENTER)

        # 민수는 회원가입창에 이름, 비번, 번호를 입력한다.
        # 그리고 회원가입 버튼을 누른다
        username_box = self.browser.find_element_by_name('username')
        password_box = self.browser.find_element_by_name('password')
        phone_box = self.browser.find_element_by_name('phone')

        username_box.send_keys('MyTestID')
        phone_box.send_keys('01011111111')
        password_box.send_keys('123')

        self.browser.find_element_by_id('button').click()

        # 닉네임 설정창으로 리다이렉트된다.
        self.assertIn('남서울 도서공유', self.browser.title)

        # 닉네임과 휴대전화번호를 설정하기 위해서 입력한다.
        nickname_box = self.browser.find_element_by_name('nickname')
        phonenumber_box = self.browser.find_element_by_name('phonenumber')

        nickname_box.send_keys('NICKNAMETEST')
        phonenumber_box.send_keys('01020302030')

        self.browser.find_element_by_id('button').click()

        # 메인페이지로 가는서 로그인이 된것을 확인하고
        # 로그아웃을 누른다.
        self.assertNotIn('회원가입', self.browser.find_element_by_tag_name('body').text)
        self.assertNotIn('로그인', self.browser.title)

        self.browser.find_element_by_id('log_out').send_keys(Keys.ENTER)

        self.assertIn('회원가입', self.browser.find_element_by_tag_name('body').text)

        # 갑자기 하기싫어져 강종해버린다.
        # self.fail('테스트가 문제없이 통과되었습니다.')

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

        username_box.send_keys('MyTestID')
        password_box.send_keys('123')

        self.browser.find_element_by_id('button').click()

        self.assertIn('남서울 도서공유', self.browser.title)

        book_sale = self.browser.find_element_by_id('book_sale')
        book_sale.send_keys(Keys.ENTER)
        self.assertIn('도서 판매', self.browser.title)

        self.fail('이게 되나')
