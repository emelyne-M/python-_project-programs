from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")




first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")  # Corrected from "fName"

# Fill form
first_name_input.send_keys("emelyne")
last_name_input.send_keys("mwiteneza")
email_input.send_keys("mwitenzaemelyne7@gmail.com")

# Submit form
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

# Optional: Keep browser open for a moment to see results
import time
time.sleep(5)

# Clean up
driver.quit()