import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path= r'D:\\webspammer\\chromedriver.exe')


while True:
  driver.get("http://azordon.cf/t/1")
  time.sleep(0.1)
  

