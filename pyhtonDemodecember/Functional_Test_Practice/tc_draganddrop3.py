from selenium.webdriver import ActionChains
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(5)

# driver.switch_to.frame("frame-one1434677811")

nof=driver.find_elements(By.TAG_NAME,"frames")

print(len(nof))

# driver.switch_to("frame-one1434677811")
# driver.find_element(By.ID,"RESULT_TextField-6").send_keys("abc@gmail.com")
print("Typed the input sucessfully")