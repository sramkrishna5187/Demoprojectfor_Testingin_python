import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
driver.maximize_window()

drp_dwn=Select(driver.find_element(By.TAG_NAME,"select"))

drp_dwn.select_by_visible_text("Saab")
print("The value Saab is selected")
time.sleep(2)
drp_dwn.select_by_value("opel")
print("The drop down opel is selected through drop down by value")
time.sleep(2)
drp_dwn.select_by_index(3)
print("The drop down opel is selected through drop down by index")
time.sleep(2)