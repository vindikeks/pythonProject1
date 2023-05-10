import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")
    x_atr = browser.find_element(By.ID, "num1")
    x = x_atr.text
    y_atr = browser.find_element(By.ID, "num2")
    y = y_atr.text
    q = int(x)+int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(q))
    submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    submit.click()
    time.sleep(10)

finally:
    browser.quit()
