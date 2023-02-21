import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
driver.maximize_window()

driver.find_element(By.ID,"idExample").click()
print("Task1:\nClicking using id Task completed successfully")

driver.back()
driver.find_element(By.CLASS_NAME,"buttonClass").click()
print("Task2:\nClicking the button using Classname completed sucessfully")
driver.back()
driver.find_element(By.NAME,"button1").click()
print("Task3:\nClicking the button using Name completed Sucessfully")
driver.back()

driver.find_element(By.LINK_TEXT,"Click this link").click()
print("Task4:\nClicking on the link completed successfully")
driver.back()
driver.close()















