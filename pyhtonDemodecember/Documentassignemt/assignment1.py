import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://blazedemo.com/")
time.sleep(3)
driver.maximize_window()
dep=Select(driver.find_element(By.NAME,'fromPort'))
dep.select_by_visible_text("Portland")
arr=Select(driver.find_element(By.NAME,"toPort"))
arr.select_by_visible_text("London")

driver.find_element(By.XPATH,"//input[@value='Find Flights']").click()

time.sleep(5)

rowlen=len(driver.find_elements(By.XPATH,'//table[@class="table"]/tbody/tr'))
print("The number of rows in webtable are:",rowlen)

for r in range(1,rowlen+1):
    flight=driver.find_element(By.XPATH,'//table[@class="table"]//tbody/tr['+str(r)+']/td[3]').text
    print(flight)
driver.find_element(By.XPATH,'//table[@class="table"]//tbody/tr[2]/td[1]').click()

time.sleep(4)
driver.find_element(By.ID,"inputName").send_keys("Ram")
driver.find_element(By.NAME,"city").send_keys("Hyderabad")
driver.find_element(By.ID,"state").send_keys("Telengana")
driver.find_element(By.ID,"creditCardNumber").send_keys("123456547461111")
driver.find_element(By.ID,"creditCardYear").clear()
driver.find_element(By.ID,"creditCardYear").send_keys("2018")
driver.find_element(By.XPATH,"//input[@value='Purchase Flight']").click()