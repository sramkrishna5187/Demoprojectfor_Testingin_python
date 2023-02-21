from time import sleep

from selenium.webdriver.chrome import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
sleep(5)


driver.find_element(By.ID,"tags").send_keys("s")
list_ele=driver.find_elements(By.XPATH,'//*[@id="ui-id-1"]//div')

for ele in list_ele:
    print(ele.text)


