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

# Open the URL
driver.get("https://rahulshettyacademy.com/angularpractice")

# Interact with the page elements
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Facundo Navarro")
driver.find_element(By.CSS_SELECTOR,"inlineRadio1").click()

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
# Optional: Add a delay to observe the result before closing the browser


time.sleep(10)

# Close the browser
driver.quit()





















time.sleep(5)
