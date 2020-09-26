from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chromedriver = '/Users/hyunjilee/Downloads/chromedriver'
# driver = webdriver.Chrome(chromedriver)
# driver.get('https://www.naver.com')

driver = webdriver.Chrome('/Users/hyunjilee/Downloads/chromedriver')
driver.get('https://www.naver.com')

elem = driver.find_element_by_name("query")  #검색창 찾기 (검색창 우클릭 > 검사해서 소스 확인필요; 대부분 name = q 임)

elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)   #엔터 입력

assert "No results found." not in driver.page_source  #페이지에 검색결과가 없으면 프로그램 중단 (확인 line)

time.sleep(2)



driver.quit


