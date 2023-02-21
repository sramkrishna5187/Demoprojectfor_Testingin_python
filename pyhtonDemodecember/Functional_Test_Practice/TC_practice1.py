from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By


driver=webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")

driver.get("https://itera-qa.azurewebsites.net/home/automation")

# This is the code to write the
# driver.find_element(By.ID,'name').send_keys("Ram")
# driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("123456789")
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("anc@123mail.com")
# driver.find_element(By.XPATH,"//input[@type='password']").send_keys("abc123")
# driver.find_element(By.XPATH,'//textarea[@id="address"]').send_keys("This is a demo application ")
# # driver.find_element(By.XPATH,"//button[@type='submit']").click()

#check whether the radio button is enabled or not and to click on the radio button

statusbutton =driver.find_element(By.XPATH,"//input[@type='radio' and @id='female']").is_displayed()
print("The female button is dispalyed:",statusbutton)

statusselected=driver.find_element(By.XPATH,"//input[@type='radio' and @id='female']").is_selected()

print("The female radio button is slected?:",statusselected)

driver.find_element(By.XPATH,"//input[@type='radio' and @id='female']").click()

statusselected2=driver.find_element(By.XPATH,"//input[@type='radio' and @id='female']").is_selected()

print("The female radio button is slected?:",statusselected2)

driver.find_element(By.XPATH,"//input[@type='radio' and @id='male']").click()

buttonother=driver.find_element(By.XPATH,"//input[@type='radio' and @id='other']").is_enabled()

print("The others radio button is displayed?:",buttonother)
