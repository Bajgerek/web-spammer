import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path= r'.\chromedriver.exe')


while True:
  driver.get("example.com")
  time.sleep(0.1)
  

