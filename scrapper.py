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
    ser = Service(os.getcwd() + "/chromedriver_mac_arm64/chromedriver.exe")
elif(platform.system() == 'Windows'):
    ser = Service(os.getcwd() + "/chromedriver_win32/chromedriver.exe")
print(ser)
driver = webdriver.Chrome( service=ser)
driver.get('https://www.swiggy.com')


driver.find_element(by = 'By.XPATH' ,value= '//*[@id="location"]').send_keys('mumbai')
driver.find_element(by = By.XPATH ,value='//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/button[1]').click

# name = driver.find_element(by=By.XPATH, value='//*[@id="firstHeading"]/span')
# print('this is print message \n', type(name))

# driver.quit()
