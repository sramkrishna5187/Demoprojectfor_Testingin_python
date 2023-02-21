from selenium import webdriver
from selenium.webdriver.common.by import By

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.maximize_window()
#get method to launch the URL
driver.get("https://testautomationpractice.blogspot.com/")
#to refresh the browser
msg1=driver.find_element(By.XPATH,"//span[normalize-space()='Message **** 12345']").text
print(msg1)
msg2=driver.find_element(By.XPATH,"//span[normalize-space()='Message &&&123456']").get_attribute('outerHTML')
print(msg2)
driver.close()