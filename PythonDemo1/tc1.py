from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj=Service("C:\selinium\chrome\chromedriver\chromedriver.exe")
#driver=webdriver.Chrome(service=serv_obj)
##driver=webdriver.Chrome()
#driver.get("https://google.com")


def launchBrowser():
   chrome_options = Options()
   chrome_options.binary_location="../Google Chrome"
   chrome_options.add_argument("disable-infobars");
   driver = webdriver.Chrome(chrome_options=chrome_options,service=serv_obj)

   driver.get("http://www.google.com/")
launchBrowser()