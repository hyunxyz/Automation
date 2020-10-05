from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/Users/hyunjilee/Downloads/chromedriver'
headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
# headless_options.add_argument('window-size=1920x1080')  #유저가 접속하는 것 처럼 세팅
# headless_options.add_argument("disable-gpu")            #그래픽카드를 안쓰겠다 화면에 보여줄게 아니니
# headless_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# headless_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(chromedriver, options=headless_options)

driver.get('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=047&aid=0002286797&date=20201004&type=1&rankingSeq=4&rankingSectionId=103')

title = driver.find_element_by_id('articleTitle')       #기사 제목 우클릭 > 검사
print (title.text)

contents = driver.find_element_by_id('articleBodyContents')
print (contents.text)

# body가 아닌 head에 소속된 태그는 get_attribute('text') 로 가져오는 경우도 있음 
# print(head_title.get_attribute('text'))

driver.quit()
