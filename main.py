import sys, os
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from twocaptcha import TwoCaptcha

API_KEY = "054a0d7bfa77cf7f4f895325d0e14fcf"

solver = TwoCaptcha(API_KEY)

driver = webdriver.Chrome(service=Service("./chromedriver.exe"))

driver.get("https://accounts.hcaptcha.com/demo")
# driver.get("https://m.kuku.lu/index.php")
# driver.get("https://m.kuku.lu")
# sleep(100000)

sitekey = driver.find_element(By.ID, "hcaptcha-demo").get_attribute("data-sitekey")

while True:
    try:
        result = solver.hcaptcha(
            sitekey=sitekey,
            url=driver.current_url
        )

    except Exception as e:
        print(e)
        # sys.exit(e)
        continue

    else:
        print("solved: " + result["code"])
        result = result["code"]
        break

try:
    driver.execute_script('var element = document.getElementsByName("g-recaptcha-response")[0];element.style.display="";')
except:
    pass

try:
    driver.execute_script('var element = document.getElementsByName("h-captcha-response")[0];element.style.display="";')
except:
    pass

try:
    driver.find_element(By.NAME, "g-recaptcha-response").send_keys(result)
except:
    pass

try:
    driver.find_element(By.NAME, "h-captcha-response").send_keys(result)
except:
    pass

driver.find_element(By.ID, "hcaptcha-demo-submit").submit()

print("aaaa")
sleep(100)

# grecaptcha = driver.find_element(By.NAME, "g-recaptcha-response")
# hcaptcha = driver.find_element(By.NAME, "h-captcha-response")
# driver.execute_script(f'arguments[0].value = "{result};"', grecaptcha)
# driver.execute_script(f'arguments[0].value = "{result};"', hcaptcha)
# driver.execute_script("var elm = document.getElementsByTagName('iframe')[0];elm.closest('form').submit();")


