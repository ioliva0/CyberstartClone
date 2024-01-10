from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import random

#this module's fucked on mac use linux or windows
#hotkeys are different anyway so it's a good idea no matter what
import keyboard

profile = webdriver.firefox.options.Options()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", "~/CyberstartClone/src/")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile)

#driver.Manage().Window.Maximize(); 
driver.maximize_window()

def waitFor(PID : tuple, time : int =10):
    wait = WebDriverWait(driver, time)
    object = wait.until(EC.presence_of_element_located(PID))
    return object    

def alert_not_present():
    return not EC.alert_is_present()

email = "kdharvey@flinthill.org"
password = "Kevinharveyiscool101!"

driver.get("https://play.cyberstart.com/sign-in")

waitFor((By.ID, "ccc-notify-accept")).click()

emailElem = driver.find_element(By.ID, "email")
emailElem.send_keys(email)
passElem = driver.find_element(By.ID, "password")
passElem.send_keys(password)
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

driver.execute_script("alert('Please complete the capcha');")

alert_present = True

WebDriverWait(driver, 5).until(EC.alert_is_present())

try:
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
except Exception:
    print("User already accepted alert")

print("waiting for field manual")

waitFor((By.LINK_TEXT, "Field Manual"), time=600).click()

for plus_sign in driver.find_elements(By.CLASS_NAME, "toggle"):
    driver.execute_script("arguments[0].scrollIntoView(true);", plus_sign)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", plus_sign)

links = []
for manual_links in driver.find_elements(By.CSS_SELECTOR, "a[href*='/field-manual/']"):
    links.append(manual_links.get_property("href"))
    
for link in links:
    print(link)

    driver.get(link)

    time.sleep(random.randrange(3, 4) / 4.0)

    keyboard.press_and_release("windows+s")

    time.sleep(random.randrange(3, 4) / 4.0)

    keyboard.press_and_release("enter")

    time.sleep(random.randrange(3, 4) / 4.0)


driver.quit()