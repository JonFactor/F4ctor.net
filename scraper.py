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
    
def findNEnter(By, value, text):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By, value)))
        driver.find_element(By, value).send_keys(text)
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.icloud.com/')

### CODE / DO STUFF
email = "Jon.Factor@outlook.com"
password = ""

findNClick(By.XPATH, '//*[@id="root"]/ui-main-pane/div/div[2]/div/div/main/div/div[2]/ui-button')
findNEnter(By.XPATH, '//*[@id="account_name_text_field"]', email)

### DO NOT DO STUFF

time.sleep(1000)

driver.quit()