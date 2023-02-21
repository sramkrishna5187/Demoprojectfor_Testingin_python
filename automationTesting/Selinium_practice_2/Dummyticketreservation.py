from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.maximize_window()
driver.find_element(By.ID,"product_550").click()
sleep(2)

print("1st one is selected")
driver.find_element(By.ID,"product_549").click()
sleep(1)
print("second webelent is selected")
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("RamaRao")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("Surapaneni")
sleep(5)
print("The names were updated sucesfully")
driver.find_element(By.XPATH,"//label[@for='sex_1']").click()
sleep(3)
print("Selected the Gender")

driver.find_element(By.XPATH,"//textarea[@name='notes']").send_keys("This is the sample notes we are writing")

sel=Select(driver.find_element(By.CLASS_NAME,"select2-search__field"))
sel.select_by_index(0)


