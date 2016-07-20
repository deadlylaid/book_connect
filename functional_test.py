from selenium import webdriver

browser = webdriver.Firefox()


#민수는 중고 도서공유 사이트가 있다는 소릴듣고 url접속을 한다.
browser.get('http://localhost:8000/')

#웹 페이지는 헤더가 '남서울 도서공유'를 표시하고 있다.
assert '남서울 도서공유' in browser.title


#민수는 회원가입을 하고싶다.
#하지만 회원가입이 없다.

#민수는 브라우저를 종료한다.
browser.quit()
