from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
#driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
print("The Login Task completed sucessfully")
driver.close()

