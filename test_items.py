import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(30)

    browser.find_element_by_class_name("btn-add-to-basket")

    assert True, "No such button"
