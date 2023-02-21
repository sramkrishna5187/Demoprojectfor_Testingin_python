from time import sleep

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()
sleep(4)
alertwindow=driver.switch_to.alert

print(alertwindow.text)

alertwindow.accept()
print("Accepted the pop up sucessfully")
driver.quit()

