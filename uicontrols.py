from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Set the path to the chromedriver executable
chromedriver_path = "C:/Users/Usuario/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start Chrome maximized
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors

# Set up the service object
service_obj = Service(chromedriver_path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractise")

options = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for option in options:
    if option.get_attribute("value") == "option2":
        option.click()
        assert option.is_selected()
        break
