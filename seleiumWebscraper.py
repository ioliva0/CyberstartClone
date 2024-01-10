from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import time
import random

import base64

import os

path = "/home/cyber/cyberstart/CyberstartClone/src/"

#this module's fucked on mac use linux or windows
#hotkeys are different anyway so it's a good idea no matter what
from pynput.keyboard import Key, Controller

keyboard_controller = Controller()

firefox_profile = FirefoxProfile()
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", path)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
options.profile = FirefoxProfile()

driver = webdriver.Firefox(options)

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

accept_cookies = waitFor((By.ID, "ccc-notify-accept"))
time.sleep(0.2)
accept_cookies.click()

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

    keyboard_controller.press(Key.ctrl)
    keyboard_controller.press("s")
    keyboard_controller.release("s")
    keyboard_controller.release(Key.ctrl)

    time.sleep(random.randrange(7, 8) / 4.0)


    link_encoded = base64.b64encode(link.encode()).decode()

    os.mkdirs("/home/cyber/cyberstart/CyberstartClone/src/" + link_encoded)

    for character in link_encoded:
        keyboard_controller.press(character)
        time.sleep(0.01)
        keyboard_controller.release(character)
        time.sleep(0.01)

    keyboard_controller.press(Key.enter)
    keyboard_controller.release(Key.enter)

    time.sleep(random.randrange(3, 4) / 4.0)


driver.quit()
