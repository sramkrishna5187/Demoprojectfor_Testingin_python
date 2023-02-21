import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Me").click()
print("Task1:\nClicking on link completed successfully")
driver.back()
driver.find_element(By.NAME,"et_pb_contact_name_0").send_keys("Abc123")
driver.find_element(By.ID,"et_pb_contact_email_0").send_keys("ram@gmail.com")
driver.find_element(By.NAME,"et_builder_submit_button").click()
print("Task2:\nEmailing is done successfully")
driver.quit()