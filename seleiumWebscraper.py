from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
email = "kdharvey@flinthill.org"
password = "Kevinharveyiscool101!"

driver = webdriver.Firefox()
driver.get("https://play.cyberstart.com/sign-in")

cookieButton = driver.find_element(By.ID, "ccc-notify-accept")
cookieButton.click()

emailElem = driver.find_element(By.ID, "email")
emailElem.send_keys(email)
passElem = driver.find_element(By.ID, "password")
passElem.send_keys(password)
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

input("enter anything to continue")

wait = WebDriverWait(driver, 10)
field_manual_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Field Manual")))
field_manual_link.click()