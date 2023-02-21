import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(5)

src_img = driver.find_element(By.XPATH, "//img[@alt='the peaks of high tatras']")
dst_elem = driver.find_element(By.ID, "trash")
print("started executing the code")
# driver.switch_to.frame("frame-one1434677811")
# driver.find_element(By.ID,"RESULT_TextField-6").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH,'//input[@id="RESULT_TextField-5"]').send_keys("Hyderabad")
# # driver.find_element(By.XPATH,'//*[@id="q26"]/table/tbody/tr[1]/td/label').click()
act = ActionChains(driver)
# act.drag_and_drop(src_img,dst_elem).perform()
act.drag_and_drop(src_img, dst_elem).perform()
print("The drag and drop image task completed sucessfully!!!!")
