import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"Tab 2").click()
# print("Tab 2 is selected")
# time.sleep(2)
# disp=driver.find_element(By.CLASS_NAME,'et_pb_all_tabs').text
# print("The content displayed there is:",disp)

ele=driver.find_element(By.LINK_TEXT,"Tab 2")

act=ActionChains(driver)
act.move_to_element(ele).click()
time.sleep(5)
disp=driver.find_element(By.CLASS_NAME,'et_pb_all_tabs').text
print("The content displayed there is:",disp)