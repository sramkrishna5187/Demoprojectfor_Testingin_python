
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,'a')
print("The total numberof links are: ",len(links))



for link1 in links:
    # print(link1.get_attribute("href"))
    print(link1.text)
    a=link1.get_attribute('href')
    print(a)
    # a.click()
    # print('Page navigated after click: ' + driver.title)
    # driver.back()
driver.quit()