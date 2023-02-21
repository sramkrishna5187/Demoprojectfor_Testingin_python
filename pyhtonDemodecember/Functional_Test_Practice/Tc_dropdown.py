import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="c:\selinium\geckodriver\geckodriver.exe")
driver.get("https://itera-qa.azurewebsites.net/home/automation")

drpcountry=Select(driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div/select"))

drpcountry.select_by_visible_text("Potugal")

time.sleep(6)
drpcountry.select_by_value("7")


