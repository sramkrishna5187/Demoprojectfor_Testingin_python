from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID,"field1").clear()
driver.find_element(By.ID,"field1").send_keys("Ram")


button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act=ActionChains(driver)
act.double_click(button).perform()