from time import sleep

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(3)
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
sleep(2)
WindowsID=driver.window_handles

for winid in WindowsID:
    driver.switch_to.window(winid)
    print(driver.title)
    if driver.title=="OrangeHRM":
        driver.close()



