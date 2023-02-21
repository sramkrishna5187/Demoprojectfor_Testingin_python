
from selenium import webdriver
from selenium.webdriver.common.by import By

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.maximize_window()

driver.get("https://www.bing.com/")
driver.maximize_window()

driver.find_element(By.ID,"sb_form_q").send_keys("selenium") #searchbox
searchitems=driver.find_elements(By.XPATH,"//ul[@id='sa_ul']/li/div")
for item in searchitems:
    print(item)

driver.close()