from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the chromedriver executable
chromedriver_path = "C:/Users/Usuario/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"


# Set up the service object
service_obj = Service(chromedriver_path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME,"blinkingText").click()

windowsopened = driver.window_handles

driver.switch_to.window(windowsopened[1])

message = driver.find_element(By.CSS_SELECTOR, ".red").text

username = message.split("at")[1].strip().split(" ")[0]

driver.close()

driver.switch_to.window(windowsopened[0])

driver.find_element(By.CSS_SELECTOR,"#username").send_keys(username)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys(username)
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)




