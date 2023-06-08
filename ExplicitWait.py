import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Path to the ChromeDriver executable
driver_path = "//Users//mac//Downloads//chromedriver_mac_arm64"
service = Service(driver_path)

# Create a new instance of the WebDriver
driver = webdriver.Chrome(service= service)

# Navigate to a webpage
driver.get("https://google.com")

driver.maximize_window()

# Wait for an element to be visible for a maximum of 10 seconds
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

# Perform actions on the element once it is visible
element.send_keys("Explicit wait")

time.sleep(5)

# Quit the WebDriver
driver.quit()
