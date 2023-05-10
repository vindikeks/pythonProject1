import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    f_button = browser.find_element(By.TAG_NAME, "button")
    f_button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_val = browser.find_element(By.ID, "input_value")
    x = x_val.text
    ans = calc(x)
    inp_row = browser.find_element(By.ID, "answer")
    inp_row.send_keys(str(ans))
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    time.sleep(5)
finally:
    browser.quit()