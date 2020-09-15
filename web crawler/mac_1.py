import time
from selenium import webdriver


driver = webdriver.Chrome('/Users/hyunjilee/Downloads/chromedriver') #ChromeDriver로 접속
driver.get('https://www.google.com')

assert "Google" in driver.title              #페이지 제목 체크 make sure it's Google website

elem = driver.find_element_by_name("q")      #검색 입력 부분에 커서 올리기 (다양한 명령을 내리기 위해 elem 변수에 할당)
elem.clear()                                #입력 부분에 default 값이 있을 수 있으므로 비움

elem.send_keys("닭가슴살")                  #검색어 입력
elem.submit()                               #검색어 실행

assert "No results found." not in driver.page_source  #검색이 제대로 됐는지 확인

time.sleep(10)
driver.close()                               #브라우저 종료
