import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
speed1 = Select(driver.find_element(By.ID,'speed'))


speed1.select_by_visible_text("Faster")

products=Select(driver.find_element(By.ID,"products"))
products.select_by_visible_text("Yahoo")

