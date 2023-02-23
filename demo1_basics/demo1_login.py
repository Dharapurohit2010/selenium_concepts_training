import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

##print the title of the page####
#print(driver.title)
#time.sleep(6) ##bala has not used it

#ele= driver.find_element(by.ID,"email")
#ele.send_keys("hello1234@gmail.com")
driver.find_element(By.ID,"email").send_keys("hello1234@gmail.com")
driver.find_element(By.ID,"pass").send_keys("welcome@1234")
time.sleep(6) ##bala hasnot used it

##login
driver.find_element(By.NAME,"login").click()
time.sleep(10)



