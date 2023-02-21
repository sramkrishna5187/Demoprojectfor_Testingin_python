from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




#driver=webdriver.Chrome("C:\selinium\chrome1\chromedriver.exe")

driver=webdriver.Chrome("C:\selinium\chrome1\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
