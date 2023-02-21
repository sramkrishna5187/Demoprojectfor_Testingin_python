
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://www.sitepoint.com/mime-types-complete-list/")
driver.maximize_window()
time.sleep(4)
nor=(driver.find_elements(By.XPATH,"//div[@class='tablenoborder']//tr"))
noc=(driver.find_elements(By.XPATH,"//div[@class='tablenoborder']//tr[1]/th"))
lor=len(nor)
loc=len(noc)
print("The total number of Rows are:",lor)
print("The number to coloumns are:",loc)

for i in nor:
    data=(driver.find_element(By.XPATH,"//div[@class='tablenoborder']/tdbody/tr[1]/th["+str(i)+"]")).text
    print(data,end='  ')