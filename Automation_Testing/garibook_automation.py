from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Open Garibook Website
driver.get("http://fe.garibook.com/")
time.sleep(2)

# Enter Phone Number
phone_input = driver.find_element(By.ID, "phone-number")  # Adjust locator as needed
phone_input.send_keys("0123456789")
time.sleep(1)

# Submit Phone Number
driver.find_element(By.ID, "submit-phone").click()  # Adjust locator as needed
time.sleep(2)

# Extract OTP from Screen
otp_element = driver.find_element(By.ID, "otp-display")  # Adjust locator as needed
otp_code = otp_element.text

# Enter OTP
otp_input = driver.find_element(By.ID, "otp-input")  # Adjust locator as needed
otp_input.send_keys(otp_code)
time.sleep(1)

# Submit OTP
driver.find_element(By.ID, "submit-otp").click()  # Adjust locator as needed
time.sleep(3)

# Select "One Way" Trip
driver.find_element(By.ID, "one-way-option").click()  # Adjust locator as needed

# Pick a Sedan
driver.find_element(By.ID, "sedan-option").click()  # Adjust locator as needed

# Enter Pickup & Drop-off Locations
pickup_input = driver.find_element(By.ID, "pickup-location")  # Adjust locator as needed
pickup_input.send_keys("Dhaka")
time.sleep(1)
dropoff_input = driver.find_element(By.ID, "dropoff-location")  # Adjust locator as needed
dropoff_input.send_keys("Chattogram")
time.sleep(1) 

# Select Date & Time s
date_input = driver.find_element(By.ID, "trip-date")  # Adjust locator as needed
date_input.send_keys("2025-02-20")
time.sleep(1)
time_input = driver.find_element(By.ID, "trip-time")  # Adjust locator as needed
time_input.send_keys("10:00 AM")
time.sleep(1)

# Apply Promo Code
promo_input = driver.find_element(By.ID, "promo-code")  # Adjust locator as needed
promo_input.send_keys("DISCOUNT10")
driver.find_element(By.ID, "apply-promo").click()  # Adjust locator as needed

time.sleep(2)

# Submit Trip Request
driver.find_element(By.ID, "submit-trip").click()  # Adjust locator as needed

# Close Browser
time.sleep(5)
driver.quit()
