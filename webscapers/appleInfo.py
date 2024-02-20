from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import    Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import OrderedDict 
import re

# WebDriverWait(web, 100).until(EC.visibility_of_element_located(By.CLASS_NAME, 'asd'))
# https://mahoningctc.com/all-staff-directory/
# https://www.google.com/search?q=

opt = Options()
driver = webdriver.Chrome(service=Service("chromedriver.exe"))