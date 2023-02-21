import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():

    def test_Login_Chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME,"Submit").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_Login_Firefox(self):
        self.driver = webdriver.firefox()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()