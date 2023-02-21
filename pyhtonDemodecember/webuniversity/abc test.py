from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get('https://event.brawlstars.com/ru/')
sleep(3)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/nav/div/div/div/div/button/div/div').click()