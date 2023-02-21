from selenium import webdriver
from selenium.webdriver.common.by import By

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
# driver=webdriver.chrome(executable_path="C:\selinium\chrome\chromedriver\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://testautomationpractice.blogspot.com/")
#to refresh the browser
# driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Hellow world")
# driver.find_element(By.NAME,'RESULT_TextField-2').send_keys("hello")
driver.find_element(By.ID,'field1').clear()
driver.find_element(By.ID,'field1').send_keys("abc")
# driver.find_element(By.ID,'datepicker').click()

driver.find_element(By.ID,'RESULT_TextField-3').send_keys("hello")

