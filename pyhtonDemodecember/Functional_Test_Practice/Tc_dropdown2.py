import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='select2-reasondummy-container']").click()

loc=driver.find_elements(By.XPATH,"//li[@class='select2-results__option']")

print("The Total number of dropdowns present is:",len(loc))

for country in loc:
    if country.text=='Other':
        country.click()
        break
print("The task finished sucessfully")
print("The ")

