from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

button_text_elt = browser.find_element_by_css_selector(".btn-add-to-basket")
button_text = button_text_elt.text

assert button_text == "Correct!", "No such button"
