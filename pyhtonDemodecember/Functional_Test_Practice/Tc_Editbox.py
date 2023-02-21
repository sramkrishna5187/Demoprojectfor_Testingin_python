from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get('https://itera-qa.azurewebsites.net/home/automation')

driver.find_element(By.ID,'name').send_keys("Manasa")
driver.find_element(By.ID,'phone').send_keys("98430216")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("ram@123.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("123456")
driver.find_element(By.ID,"address").send_keys("This is the dummy creation for testing purpose")

driver.find_element(By.NAME,"submit").click()

print("the submission form is given sucessfully")
