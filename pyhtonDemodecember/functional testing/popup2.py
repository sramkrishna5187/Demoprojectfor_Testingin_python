from time import sleep

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button').click()
sleep(4)
alertwindow=driver.switch_to.alert

alertwindow.dismiss()
print("The alert is dismissed")
sleep(3)

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
alertwindow2=driver.switch_to.alert
sleep(3)
alertwindow2.send_keys("This is my msg")
sleep(6)
alertwindow2.accept()
