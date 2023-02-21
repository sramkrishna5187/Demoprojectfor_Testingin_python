from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
global driver
#serv_obj=Service("C:\selinium\chrome\chromedriver\chromedriver.exe")
#driver=webdriver.Chrome(service=serv_obj)
driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
