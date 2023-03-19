from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import platform

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

global ser
if(platform.system() == 'Darwin'):
    ser = Service(os.getcwd() + "/chromedriver_mac_arm64/chromedriver")
elif(platform.system() == 'Windows'):
    ser = Service(os.getcwd() + "/chromedriver_win32/chromedriver.exe")
print(ser)
driver = webdriver.Chrome(options=options , service=ser)
driver.get('https://en.wikipedia.org/wiki/Wikipedia')

driver.find_element(by = 'By.XPATH' ,value= '//*[@id="searchform"]/div/div/div[1]/input').send_keys('leo')
# driver.find_element(by = By.XPATH ,value='//*[@id="searchform"]/div/button').click

name = driver.find_element(by=By.XPATH, value='//*[@id="firstHeading"]/span')
# print('this is print message \n', type(name))

driver.quit()
