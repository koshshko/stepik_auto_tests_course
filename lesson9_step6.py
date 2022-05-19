from selenium import webdriver
import time
import math
import os
import math

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(chrome_options=chrome_options)

link = "http://suninjuly.github.io/redirect_accept.html"

try:    
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    browser.switch_to.window(browser.window_handles[1])
    new_window = browser.window_handles[0]

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()