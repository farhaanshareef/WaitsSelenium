from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver_path = "//Users//mac//Downloads//chromedriver_mac_arm64"
service = Service(driver_path)

# Create a new instance of the WebDriver
driver = webdriver.Chrome(service= service)

# Navigate to a webpage
driver.get("https://google.com")

# Define the FluentWait with a maximum timeout of 20 seconds and a polling interval of 2 seconds
wait = WebDriverWait(driver, timeout=20, poll_frequency=2)

# Wait until an element with the ID "myElementId" is visible
element = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

# Perform actions on the element once it is visible
element.click()

# Quit the WebDriver
driver.quit()
