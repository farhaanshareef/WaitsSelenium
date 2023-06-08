# Importing the necessary modules from Selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Path to the ChromeDriver executable
driver_path = "//Users//mac//Downloads//chromedriver_mac_arm64"
service = Service(driver_path)

# Creating a new instance of the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Opening the Google homepage
driver.get("https://google.com")

# Maximizing the browser window
driver.maximize_window()

# Setting the implicit wait time to 10 seconds
driver.implicitly_wait(10)

# Finding the element with the given XPath and inputing data on it
driver.find_element(By.NAME, "q").send_keys("Implicit wait")

time.sleep(5)
