import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from Selinium_practice_2.DataDrivenTesting import XlUtils

# serv_obj=Service("C:\selinium\chrome1\chromedriver.exe")
# driver=webdriver.chrome(service=serv_obj)

driver=webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(4)

file="C:\selinium\Data\caldata2.xlsx"
rows=XlUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    Principal=XlUtils.readData(file,"Sheet1",r,1)
    ROI=XlUtils.readData(file,"Sheet1",r,2)
    Period1=XlUtils.readData(file,"Sheet1",r,3)
    Period2 =XlUtils.readData(file, "Sheet1",r,4)
    Freq=XlUtils.readData(file, "Sheet1",r,5)
    exp_val=XlUtils.readData(file, "Sheet1",r,6)

    time.sleep(10)

    #pass the value to the application
    driver.find_element(By.XPATH,"//*[@id='principal']").send_keys(Principal)
    driver.find_element(By.XPATH,"//*[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH,'//*[@id="tenure"]').send_keys(Period1)
    per=Select(driver.find_element(By.XPATH,'//*[@id="tenurePeriod"]'))
    per.select_by_visible_text(Period2)
    frequency=Select(driver.find_element(By.XPATH,'//*[@id="tenurePeriod"]'))
    frequency.select_by_visible_text(Freq)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    Act_val=driver.find_element((By.XPATH,'resp_matval')).text

    if float(exp_val)== float (Act_val) :
        print("The test case is passed")
        XlUtils.writeData(file,'Sheet1',2,8,"Passed")
        XlUtils.fillGreenColor(file,'Sheet1',8)
    else:
        print("The Test case is failed")
        XlUtils.writeData(file,'Sheet1',2,8,"Failed")
        XlUtils.fillRedColor(file,'Sheet1',8)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)
driver.close()











