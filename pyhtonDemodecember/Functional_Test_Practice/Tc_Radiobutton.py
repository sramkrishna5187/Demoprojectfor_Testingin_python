from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.get("https://itera-qa.azurewebsites.net/home/automation")

driver.find_element(By.XPATH,"//input[@id='female']").click()
driver.find_element(By.XPATH,'//*[@id="tuesday"]').click()
