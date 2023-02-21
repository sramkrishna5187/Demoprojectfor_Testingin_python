from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

src_ele=driver.find_element(By.XPATH,'//*[@id="draggable"]/p')

dst_ele=driver.find_element(By.XPATH,'//*[@id="droppable"]')

act=ActionChains(driver)
act.drag_and_drop(src_ele,dst_ele).perform()

print("The task completed succesfully!!!")
