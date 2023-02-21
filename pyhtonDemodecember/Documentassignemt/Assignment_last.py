import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys('secret_sauce')
driver.find_element(By.ID,"login-button").click()

# Entered into the login page
header = driver.find_element(By.XPATH,"//span[@class='title']").text
print("The header of the webpage is :"+header)

sort = Select(driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
sort.select_by_value("az")
print("sort by name selected")
time.sleep(5)
sort.select_by_value("za")
print("sort by name selected")
time.sleep(5)

#sort.select_by_value("lohi")

print("sort by Price")
time.sleep(5)

article=driver.find_elements(By.TAG_NAME,"button")

for c in article:
    print("The item working on now is:",c.get_attribute("name"))
    item=c.get_attribute("name")
    if item=="add-to-cart-sauce-labs-bike-light":
        c.click()
        break
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()

driver.find_element(By.ID,"checkout").click()
driver.find_element(By.ID,"first-name").send_keys("Rama")
driver.find_element(By.ID,"last-name").send_keys("sriRam")
driver.find_element(By.ID,"postal-code").send_keys("524999")
driver.find_element(By.ID,"continue").click()
time.sleep(3)
driver.find_element(By.ID,"finish").click()
print("Hurrah!!! \n The task is completed sucessfully")
