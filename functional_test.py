from selenium import webdriver
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
        self.fail('Finish the test!')

        # 민수는 회원가입을 하고싶다.
        # 하지만 회원가입이 없다.

        # 민수는 브라우저를 종료한다.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
