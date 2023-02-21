import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get("http://webdriveruniversity.com/index.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//h1[normalize-space()='DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)']").click()
time.sleep(2)
p = driver.current_window_handle
chld = driver.window_handles[1]
driver.switch_to.window(chld)
print(driver.title)
#lan=Select(driver.find_element(By.ID,"dropdowm-menu-1"))
lan=Select(driver.find_element(By.ID,"dropdowm-menu-1"))
lan.select_by_visible_text("Python")
print("Dropdown Python is selected")
time.sleep(3)
lan.select_by_visible_text("SQL")
print("\nDropdown SQL is selected")

ide=Select(driver.find_element(By.ID,"dropdowm-menu-2"))
ide.select_by_value("testng")
print("\n Dropdown TestNG is selected")
time.sleep(2)
fes=Select(driver.find_element(By.ID,"dropdowm-menu-3"))
fes.select_by_visible_text("CSS")
print("\nCSS is selected in drop down")
# time.sleep(2)
# driver.find_element(By.XPATH,'//input[@value="option-2"]').click()
# print("Checkbox is selected successfully")
#
# chekbox=driver.find_element(By.XPATH,'//input[@value="option-3"]').is_selected()
# print("is checkbox3 is checked?:",chekbox)
#
# time.sleep(3)
#
# driver.find_element(By.XPATH,'//input[@value="pumpkin"]').click()
# print("The radio button pumpkin got selected")
# time.sleep(2)
# driver.find_element(By.XPATH,'//input[@value="lettuce"]').click()
# print("The selectbox luttuce got selected")
# time.sleep(2)
# btn_sel=driver.find_element(By.XPATH,'//input[@value="cabbage"]').is_selected()
# print("the button is diabled:",btn_sel)
#
# fruit=Select(driver.find_element(By.ID,'fruit-selects'))
# fruit.select_by_visible_text("Pear")
# print("The fruit pear got selected")

driver.close()





