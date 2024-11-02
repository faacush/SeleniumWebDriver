from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

# Set the path to the chromedriver executable
chromedriver_path = "C:/Users/Usuario/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"


# Set up the service object
service_obj = Service(chromedriver_path)
sorted_fruits = []
# Initialize the Chrome driver
driver = webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

fruits = driver.find_elements(By.XPATH,"//tr/td[1]")

for fruit in fruits:
    sorted_fruits.append(fruit.text)

browsersortedlist = sorted_fruits.copy()

sorted_fruits.sort()

assert sorted_fruits == browsersortedlist
    