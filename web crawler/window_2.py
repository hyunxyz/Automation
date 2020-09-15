import time
from selenium import webdriver

# 절대경로 지정할 경우 (파일생성 > 드라이버파일 옮김 > 경로 복사 )
driver = webdriver.Chrome(executable_path='C:/Users/admin/Downloads/chromedriver/chromedriver.exe')
driver.get('https://www.naver.com')  #이동

time.sleep(2)

driver.close()                       #quit도 가능
