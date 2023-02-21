from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
