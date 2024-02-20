from django.shortcuts import render

# Create your views here.

class AppleInfoView ():
    def post(self, request):
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

        driver.get("https://twitter.com/home")
        driver.add_cookie({"name": "auth_token", "value": "e7ce82e905a277de84c2ab50ae0fa74d9d7f38eb"})
        time.sleep(2)
        driver.refresh()

        driver.get("https://twitter.com/MonKeyM36809001/likes")

        time.sleep(3)
        LikedContainer = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div')
        LikedContainerInners = []
        i = 1
        while True:
            try:
                element = driver.find_element(By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{i}]')
                LikedContainerInners.append(element)
                i += 1
            except Exception:
                break
                
        for ContinerInner in LikedContainerInners:
            try:
                time.sleep(1)
                Video = ContinerInner.find_element(By.CLASS_NAME, "css-1dbjc4n r-1p0dtai r-1loqt21 r-1d2f490 r-u8s1d r-zchlnj r-ipm5af")
                print(Video)
                time.sleep(1)
                driver.get("https://twitter.com/MonKeyM36809001/likes")
            except Exception as ex:
                print(ex)

        time.sleep(1000)

        driver.quit()

