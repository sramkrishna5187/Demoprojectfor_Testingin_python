from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://itera-qa.azurewebsites.net/home/automation")

oneyr=driver.find_element(By.XPATH,'/html/body/div/div[5]/div[2]/div[1]/div[1]/label').is_enabled()

print("The status of one year webbutton is ",oneyr)

noneyr=driver.find_element(By.XPATH,"//label[@for='none']").is_enabled()
nonebutton=driver.find_element(By.XPATH,"//label[@for='none']").is_selected()

print("The status of none webbutton is ",noneyr)

print("The status of none button is selected is",nonebutton)