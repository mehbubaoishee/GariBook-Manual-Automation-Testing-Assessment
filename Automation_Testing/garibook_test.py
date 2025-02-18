from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Garibook website
driver.get("http://fe.garibook.com/")

# Click on the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
)
login_button.click()

# Enter phone number
phone_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "mobile"))
)
phone_input.send_keys("01994050014")  # Replace with actual phone number

# Click Send Code button
send_code_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send Code')]")
send_code_button.click()

# Wait for OTP to appear and extract it
otp_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "alert-info"))
)
otp_text = otp_element.text
otp = otp_text.split(": ")[1].strip()

# Enter OTP
otp_inputs = driver.find_elements(By.CLASS_NAME, "text-center")
for i in range(4):
    otp_inputs[i].send_keys(otp[i])

# Click Continue button
continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
continue_button.click()

# Wait for redirection to home page
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
).click()

# Enter Pickup Location
pickup_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "pickup_location"))
)
pickup_input.send_keys("Mirpur-1, Dhaka, Bangladesh")
time.sleep(2)  # Wait for suggestion dropdown
pickup_input.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

# Enter Drop-off Location
dropoff_input = driver.find_element(By.NAME, "drop_off_location")
dropoff_input.send_keys("Gulshan 1, Dhaka, Bangladesh")
time.sleep(2)
dropoff_input.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

# Select Date
date_input = driver.find_element(By.NAME, "pickup_date_time")
date_input.send_keys("19/02/2025, 10:00 AM")  # Adjust time if needed

time.sleep(1)

# Enter Promo Code
promo_input = driver.find_element(By.NAME, "promo_code")
promo_input.send_keys("Oishee")

# Click Submit button
submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
submit_button.click()

# Wait for confirmation
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "confirmation-message"))
)

print("Trip booking completed successfully!")

driver.quit()