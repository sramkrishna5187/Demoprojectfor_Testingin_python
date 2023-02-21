import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
#
# driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
#
# time.sleep(3)
#
# date="14"
# month='Sep'
# year="1990"
# while True:
#
#     wm=driver.find_element(By.XPATH,"//*[@class='ui-datepicker-month']").text
#     wy=driver.find_element(By.XPATH,"//*[@class='ui-datepicker-year']").text
#     print(wm)
#     print(wy)
#     if wm==month and wy==year:
#       break;
#     else:
#         print("Else step is executed sucessfully")
#         driver.find_element(By.XPATH,"//*[@class='ui-datepicker-prev ui-corner-all']").click()
#     dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/a")
#     print("Date step executed sucessfully")
#     for wdate in dates:
#         if date==wdate:
#             wdate.click()
#             break;
#
#
#
#

test=driver.find_element(By.XPATH,"//span[normalize-space()='Message **** 12345']").get_attribute("style")
print(test)

test1=driver.find_element(By.XPATH,"//span[normalize-space()='Message **** 12345']").text
print(test1)