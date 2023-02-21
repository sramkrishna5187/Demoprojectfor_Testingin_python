import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\\selinium\\chrome1\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\\selinium\\geckodriver\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):       # This will return the Browser value to setup method
    return request.config.getoption("--browser")





