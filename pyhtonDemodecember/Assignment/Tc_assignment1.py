import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get('https://admin-demo.nopcommerce.com/login')
time.sleep(3)
driver.find_element(By.ID,'Email').clear()
driver.find_element(By.ID,'Email').send_keys("admin@yourstore.com")
driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(3)

dashvalue=driver.find_element(By.XPATH,"//h1[normalize-space()='Dashboard']").text

assert("Dashboard",dashvalue)

print(dashvalue)