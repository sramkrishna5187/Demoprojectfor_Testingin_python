import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@value='male']").click()
print("clicked on Male radio button successfully")

f_btn=driver.find_element(By.XPATH,'//input[@value="female"]').is_displayed()
print("The female radio button is displayed:",f_btn)

othr_btn=driver.find_element(By.XPATH,'//input[@value="other"]').is_selected()
print("The other radio button is selected?",othr_btn)

driver.find_element(By.XPATH,'//input[@value="other"]').click()
othr_btn=driver.find_element(By.XPATH,'//input[@value="other"]').is_selected()
print("The other radio button is selected?",othr_btn)
##Task on check boxes

driver.find_element(By.XPATH,'//input[@value="Bike"]').click()
print("The check box I have Bike is selected")
chk_car=driver.find_element(By.XPATH,'//input[@value="Car"]').is_selected()
print("The check box I have car is selected?:",chk_car)
driver.find_element(By.XPATH,'//input[@value="Car"]').click()
chk_car=driver.find_element(By.XPATH,'//input[@value="Car"]').is_selected()
print("The check box I have car is selected?:",chk_car)


driver.close()


