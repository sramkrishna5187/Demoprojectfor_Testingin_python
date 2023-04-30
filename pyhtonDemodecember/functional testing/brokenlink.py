import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in allLinks:
    url=link.get_attribute('href')

    res=requests.head(url)


    if res.status_code>=400:
        print(url,res.status_code,"  is broken link")
        count+=1
    else:
        print(url,res.status_code,"   is valid link")

print("Total number of broken links:",count)
