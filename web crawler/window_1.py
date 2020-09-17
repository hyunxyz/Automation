from selenium import webdriver

# working directory안에 chromedriver.exe 파일을 directly 넣을 경우 (VSCode explorer 창에 드랙드롭)
browser = webdriver.Chrome('chromedriver')

search_term = '스마트팜'
url = "https://www.google.co.in/search?q=" + search_term + "&tbm=isch"
browser.get(url)        #url로 이동