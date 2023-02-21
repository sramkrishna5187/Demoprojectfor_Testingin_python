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

driver.find_element(By.XPATH,"//h1[normalize-space()='ACTIONS']").click()
time.sleep(2)
chld=driver.window_handles[1]
driver.switch_to.window(chld)
print(driver.title)

src=driver.find_element(By.XPATH,"//div[@id='draggable']//p")
dst=driver.find_element(By.XPATH,"//div[@id='droppable']//p")

act=ActionChains(driver)
act.drag_and_drop(src,dst).click().perform()
print("The drag drop act completed succesfully")
time.sleep(2)
# dbl_clk=driver.find_element(By.XPATH,'//div[@id="double-click"]')
# act.double_click(dbl_clk).perform()
# print("The task double click performed successfully")

# hov1=driver.find_element(By.XPATH,"//button[normalize-space()='Hover Over Me First!']")
# hova=driver.find_element(By.XPATH,"//div[@class='dropdown hover']//a[@class='list-alert'][normalize-space()='Link 1']")
# act.move_to_element(hov1).move_to_element(hova).click().perform()
# print("The mouse hover for the element 1 completed successfully!!")
# alert1=driver.switch_to.alert
# txt1=alert1.text
# time.sleep(3)
# alert1.accept()
# print(txt1)
abc = driver.find_element(By.ID,"click-box").click()
# act.move_to_element(abc).perform()
# act.double_click(abc).perform()

print("Double click happened!!!!")