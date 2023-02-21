from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.maximize_window()

driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.NAME,"q").send_keys("selenium") #searchbox
searchitems=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li/div/div[2]")

print(len(searchitems))

for item in searchitems:
    print(item.text)
    if item.text=='selenium':
        item.click()
        break