import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com/")

##clickon create new account
##enter firstname as john
driver.find_element(By.LINK_TEXT,"Create new account").click()
#time.sleep(5)
driver.find_element(By.NAME,"firstname").send_keys("John")
driver.find_element(By.NAME,"lastname").send_keys("dina")
driver.find_element(By.NAME,"reg_email__").send_keys("dhara.pandit@einfochips.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys("welcome123")
driver.find_element(By.XPATH,"//input[@value='-1']").click()

####click on sign up
driver.find_element(By.NAME,"websubmit").click()
time.sleep(5)
