
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.maximize_window()

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

dropdown=Select(driver.find_element(By.XPATH,"//select[@class='custom-select']"))

drp=dropdown.options
print("The total number of dropdown of elements",len(drp))

for con in drp:
    if "Greece"==con.text:
        con.click()
        print("The selection of the country is succesful")
        break

options=driver.find_elements(By.XPATH,"//select[@class='custom-select']")

print(len(options))
print(options)





