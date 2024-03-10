from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import OrderedDict 
import re
from selenium.webdriver.common.keys import Keys

# WebDriverWait(web, 100).until(EC.visibility_of_element_located(By.CLASS_NAME, 'asd'))
# https://mahoningctc.com/all-staff-directory/
# https://www.google.com/search?q=

def findNClick(By, value):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By, value)))
        driver.find_element(By, value).click()
        return True
    except:
        return False
    
def findNEnter(By, value, text, enter):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By, value)))
        driver.find_element(By, value).send_keys(text)
        if enter:
            driver.find_element(By, value).send_keys(Keys.ENTER)
        return True
    except:
        return False

def findNReturn(By, value):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By, value)))
        return driver.find_element(By, value)
    except:
        return None

opt = Options()
opt.headless = True
driver = webdriver.Chrome(service=Service("C:\\Users\\jonfa\\OneDrive\\Documents\\GitHub\\F4ctor.net\\webscapers\\chromedriver.exe"))
driver.get('https://www.googlemaps.com/')

### CODE / DO STUFF

### DO NOT DO STUFF

time.sleep(1000)

driver.quit()