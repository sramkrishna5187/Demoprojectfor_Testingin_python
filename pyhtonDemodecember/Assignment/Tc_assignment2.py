import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\selinium\geckodriver\geckodriver.exe")
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')

time.sleep(3)

driver.find_element(By.ID, "select2-billing_state-container").click()
loc = driver.find_elements(By.CLASS_NAME, "select2-results__option")

driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys("Bihar")
driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()

# lc = loc.options
# print ("The number of states in the list are:",len(lc))
# for country in loc:
#     if country.text() == "Assam":
#         country.click()
