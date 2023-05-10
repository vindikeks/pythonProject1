import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    f_name = browser.find_element(By.NAME, "firstname")
    f_name.send_keys("qwdqd")
    l_name = browser.find_element(By.NAME, "lastname")
    l_name.send_keys("fdhhf")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("ehfd@sgf.com")
    f_send = browser.find_element(By.ID, "file")
    f_send.send_keys(file_path)
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    time.sleep(7)
finally:
    browser.quit()

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
