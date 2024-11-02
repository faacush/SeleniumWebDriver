from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

# Open the URL
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT,"forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.coms")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello123")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()











time.sleep(3)