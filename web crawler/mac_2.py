import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/hyunjilee/Downloads/chromedriver')
driver.get('https://www.instagram.com')
                                                    #IG > F12 > 좌측상단 커서아이콘 > 원하는 칸 클릭
driver.implicitly_wait(3)                           #웹페이지가 로딩될 때 까지 기다림
time.sleep(3)

driver.find_element_by_name('username').send_keys('myle.index')   #페이지별 코드에 따라 name 이외 다른 명칭일 수 있음 (XPath,Id)
driver.find_element_by_name('password').send_keys('FMsptkdtm7.')

driver.find_element_by_xpath("//button[@type='submit']").click()    #구글링한 xpath.. 실제 값 입력시 오류뜸?
time.sleep(3)

# //*[@id="loginForm"]/div/div[3]/button/div           #F12 > 해당 코드 > 우클릭 > Copy > Copy in XPath ??

driver.get_screenshot_as_file('capture.png')

driver.quit()




# elem_id = driver.find_element_by_name('username')
# elem_pw = driver.find_element_by_name('password')

# elem_id.send_keys('myle.index')
# elem_pw.send_keys('FMsptkdtm7.')

# elem_pw.submit()
# time.sleep(3)

# login_btn = driver.find_element_by_name('log.login')

