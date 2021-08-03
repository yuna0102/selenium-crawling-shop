from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login import my_id, my_pw
import time
import os
import pyperclip

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("no-sandbox")
chrome = webdriver.Chrome("./chromedriver.exe", options=options)
wait = WebDriverWait(chrome, 30)
short_wait = WebDriverWait(chrome, 5)

chrome.get("http://shopping.naver.com")


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

#pip install pyperclip
#붙여넣기 하겠다는 뜻
pyperclip.copy('mkiyg')
input_id.send_keys(Keys.CONTROL + "v")

pyperclip.copy('phgbbynl0102^0^w')
input_pw.send_keys(Keys.CONTROL + 'v')

input_pw.send_keys("\n")

#로그아웃 버튼
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button")))

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys("아이폰 케이스")
time.sleep(1)
search.send_keys("\n")

#리스트들을 돌기 기다리면서 
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class^=basicList_link__]")))
#리스트 제목을 다 가져와줌
titles = chrome.find_elements_by_css_selector("a[class^=basicList_link__]")
for title in titles:
    print(title.text)

chrome.close()

# #선택자 불러오는 방법
# a.logout_button
# a[class="logout_button"]
# a[class^="logout"] #logout으로 시작하는
# a[class$="button"] #button으로 끝나는
# a[class*="out_but"] #out_but이라는 단어가 들어있는