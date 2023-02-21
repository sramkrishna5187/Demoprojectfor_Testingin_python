from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.maximize_window()

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

alldays=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

for day in alldays:
    weekname=day.get_attribute('id')
    print(weekname)
    # if weekname=='tuesday':
    day.click()
for checkbox in alldays:
    if checkbox.is_enabled():
        checkbox.click()
        


driver.quit()




