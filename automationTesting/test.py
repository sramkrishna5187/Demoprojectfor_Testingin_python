from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https:\\www.amazon.in")



print("Login of the page successful")


driver.find_element(By.LINK_TEXT,"Today's Deals").click()

driver.get("http://www.automationpractice.com")

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-description")
print(len(sliders))
driver.close()
