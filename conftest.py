import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', default=None)

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', [user_language])
def test_basket_button(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
