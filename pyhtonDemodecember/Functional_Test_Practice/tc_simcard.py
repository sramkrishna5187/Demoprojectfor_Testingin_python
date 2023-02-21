import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.maximize_window()

driver.get("https://www.google.co.in")
driver.find_element(By.XPATH,"//input[@title='Search']").send_keys("Bsnl new sim")
driver.find_element(By.XPATH,"//input[@title='Search']").send_keys(Keys.RETURN)

time.sleep(4)

driver.find_element(By.XPATH,"//h3[contains(text(),'BSNL')]").click()