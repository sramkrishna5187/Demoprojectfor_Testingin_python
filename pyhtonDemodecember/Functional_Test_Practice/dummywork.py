import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

time.sleep(3)

driver.find_element(By.ID,"select2-billing_country-container").click()

loc=driver.find_elements(By.XPATH,"//li[@class='select2-results__option' ]")


for country in loc:
    print(country.text)
    if country.text=="Iraq":
        country.click()
        break;


print("The completed sucessfully!!!")