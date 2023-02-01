from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
pass_input = os.environ.get("PASSWORD")
email_input = os.environ.get("EMAIL")
chrome_path = Service(r"C:\Users\91767\Downloads\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
to_find_url = input("ENTER NAME:")
if to_find_url:
    driver = webdriver.Chrome(service=chrome_path, options=op)
    driver.get("https://www.google.com/")
    search = driver.find_element(by=By.NAME, value="q")
    search.send_keys(f"{to_find_url}")
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(6)
    link = driver.find_element(by=By.CLASS_NAME, value="yuRUbf")
    url = link.text
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    print(urls[0])
    driver.get(urls[0])
    login = driver.find_element(by=By.NAME, value="email")
    login.send_keys(email_input)
    password = driver.find_element(by=By.NAME, value="pass")
    password.send_keys(pass_input)
    sign_in = driver.find_element(by=By.NAME, value="login").click()

