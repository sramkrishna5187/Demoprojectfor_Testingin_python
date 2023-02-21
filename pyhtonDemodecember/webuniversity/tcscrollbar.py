import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("http://webdriveruniversity.com/index.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//h1[normalize-space()='SCROLLING AROUND']").click()
time.sleep(3)
driver.execute_script("window.scrollTo(615, 3000);")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #3000