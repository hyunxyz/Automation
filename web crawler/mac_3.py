from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chromedriver = '/Users/hyunjilee/Downloads/chromedriver'
# driver = webdriver.Chrome(chromedriver)
# driver.get('https://www.naver.com')

driver = webdriver.Chrome('/Users/hyunjilee/Downloads/chromedriver')
driver.get('https://www.naver.com')

print(driver.title)
print(driver.current_url)

assert "NAVER" in driver.title              #make sure 타이틀에 NAVER 문구가 있는지

elem = driver.find_element_by_name("query") #검색창 찾기 (검색창 우클릭 > 검사해서 소스 확인필요; 대부분 name = q 임)
                              #페이지마다 데이터 태그방법이 다름 (id, name, tag_name ...)
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)                 #엔터 입력

time.sleep(2)

assert "No results found." not in driver.page_source  #페이지에 "No~"가 발견되지 않으면 다음 라인으로 넘어가라 ('make sure' line)

driver.quit()