from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

month="March"
year="1990"
date="5"
#driver.find_element(By.ID,"datepicker").send_keys("15/03/1990")
driver.find_element(By.ID,"datepicker").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if month==mon and year==yr:
        break
    else:
     driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]/span').click()

# to select the date



dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break

print("The task completed sucessfully")
