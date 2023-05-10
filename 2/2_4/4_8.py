import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
sel = browser.find_element(By.ID, "book")
sel.click()
x_val = browser.find_element(By.ID, "input_value")
x = x_val.text
ans = calc(x)
inp_row = browser.find_element(By.ID, "answer")
inp_row.send_keys(str(ans))
submit = browser.find_element(By.ID, "solve")
submit.click()
time.sleep(10)
