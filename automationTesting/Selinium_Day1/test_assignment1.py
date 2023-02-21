from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

driver.find_element(By.ID,"name").send_keys("Rama")
driver.find_element(By.ID,"phone").send_keys("9847890")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("123@xyz.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("krishna")
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("This is a dummt test created")
driver.find_element(By.NAME,"submit").click()


