from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID,'field1').clear()
driver.find_element(By.ID,'field1').send_keys("abc")
driver.find_element(By.ID,'datepicker').click()
print("The date picker box clicked sucessfully")