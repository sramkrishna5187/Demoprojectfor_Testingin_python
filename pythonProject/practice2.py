from time import time, sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
f=driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[1]/label")
if f.is_enabled()== True :
    f.click()
sleep(4)
driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[2]/label").click()
otr=driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[3]/label").is_displayed()

if True == otr:
    print("Other display is enabled")
else:
    print("Other : dispaly is disabled")

driver.close()


