# DemoWebDriver.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

#이 부분을 수정한다. 
driver = set_chrome_driver()
driver.implicitly_wait(3)
#driver.get('https://google.com')
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('kim')
driver.find_element_by_name('pw').send_keys('1234')
