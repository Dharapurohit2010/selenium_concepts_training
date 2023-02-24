import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
###enter first name
driver.find_element(By.NAME,"UserFirstName").send_keys("john")
driver.find_element(By.NAME,"UserLastName").send_keys("sina")
driver.find_element(By.NAME,"UserEmail").send_keys("dfgfddf@gmail.com")
select_jobtitle = Select(driver.find_element(By.NAME,"UserTitle"))
select_jobtitle.select_by_visible_text("Sales Manager")
driver.find_element(By.NAME,"CompanyName").send_keys("abc")
select_employee= Select(driver.find_element(By.NAME,"CompanyEmployees"))
select_employee.select_by_visible_text("501 - 1500 employees")
driver.find_element(By.NAME,"UserPhone").send_keys("8876788")
select_country=Select(driver.find_element(By.NAME,"CompanyCountry"))
select_country.select_by_visible_text("Afghanistan")
driver.find_element(By.CLASS_NAME, "checkbox-ui").click()
driver.find_element(By.NAME, "start my free trial").click()
time.sleep(5)


