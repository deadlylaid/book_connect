from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_sign_up_this_website(self):

        # 민수는 중고 도서공유 사이트가 있다는 소릴듣고 url접속을 한다.
        self.browser.get('http://localhost:8000/')

        # 웹 페이지는 헤더가 '남서울 도서공유'를 표시하고 있다.
        self.assertIn('남서울 도서공유', self.browser.title)

        # 민수는 회원가입을 하고싶다.
        # 민수는 회원가입 버튼을 누른다.
        join_us = self.browser.find_element_by_id('join_us')
        join_us.send_keys(Keys.ENTER)

        # 갑자기 하기싫어져 강종해버린다.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
