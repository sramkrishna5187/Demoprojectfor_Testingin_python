import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://www.christmassongsandcarols.com/products/jingle-bells-lyrics")
Numberoflinks=driver.find_elements(By.TAG_NAME,'a')

print("The total number of links in the given webpage are:",len(Numberoflinks))

for link in Numberoflinks:

    url=link.get_attribute("href")
    result=requests.head(url)
    print(link.text)
    if result=="200" :
        print(url,"The link is valid")
    else:
        print(url,"The link is invalid")

