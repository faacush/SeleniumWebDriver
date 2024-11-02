from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

# Set the path to the chromedriver executable
chromedriver_path = "C:/Users/Usuario/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--start-maximized")
Chrome_options.add_argument("headless")
Chrome_options.add_argument("--ignore-certificate-errors")



# Set up the service object
service_obj = Service(chromedriver_path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service_obj, options=Chrome_options)


driver.get("https://rahulshettyacademy.com/angularpractice/")


print(driver.title)
