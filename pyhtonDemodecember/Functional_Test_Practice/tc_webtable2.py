
from selenium import webdriver

from selenium.webdriver.common.by import By


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("https://www.sitepoint.com/mime-types-complete-list/")
driver.maximize_window()
nor=len(driver.find_elements(By.XPATH,"//div[@class='tablenoborder']//tr"))
noc=len(driver.find_elements(By.XPATH,"//div[@class='tablenoborder']//tr[1]/td"))
d1=data=driver.find_element(By.XPATH,"//div[@class='tablenoborder']//tbody/tr[5]/td[2]").text
print(d1)
print(nor,noc)

#
for r in range(2,nor+1):
    for c in range(1,noc+1):
        print(str(r))
        print(str(c))
        data=driver.find_element(By.XPATH,"//div[@class='tablenoborder']//tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end="    ")
