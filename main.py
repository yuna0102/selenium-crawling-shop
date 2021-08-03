from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("no-sandbox")
chrome = webdriver.Chrome("./chromedriver.exe", options=options)
chrome.get("http://shopping.naver.com")
wait = WebDriverWait(chrome, 10)
#아래 코드의 반응값이 바로 element를 찾는 것임
el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
print(el)
chrome.close()