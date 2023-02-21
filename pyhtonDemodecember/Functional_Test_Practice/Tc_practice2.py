from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.get("https://itera-qa.azurewebsites.net/home/automation")

#check box and radio box using xpath

driver.find_element(By.XPATH,"//label[@for='1year']").click()
sleep(5)

seloneyr=driver.find_element(By.XPATH,"//label[@for='1year']").is_selected()
print("The value for the first year is selected?: ",seloneyr)

driver.find_element(By.XPATH,'//LABEL[@FOR="3years"]').click()

displaynone=driver.find_element(By.XPATH,'//label[@for="none"]').is_enabled()
print("The raido button is enabled ?:",displaynone)


displayheader=driver.find_element(By.XPATH,'//label[@for="tools"]').text
print("The name displayed as :",displayheader)


#selecting id


# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#
# for day in checkboxes:
#     day.click()
#     print("The day got selceted is:",day.get_attribute('id'))

# listframework=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @class='custom-control-input']")
#
# for fw in listframework:
#     fw.click()
#     print("The framework selected is :",fw.get_attribute('id'))

driver.find_element(By.XPATH,"//label[@for='serenity']").click()

