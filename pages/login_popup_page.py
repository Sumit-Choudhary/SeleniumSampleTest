from Resources.Locators import LoginPageLocators as login_page
from base.selenium_base import SeleniumBase


class LoginPopupPage():
    def __init__(self):
        global driver, selenium_base
        selenium_base = SeleniumBase()
        driver = selenium_base.get_driver()

    def load_flipkart(self, url):
        driver.get(url)

    def login_to_account(self, username, pwd):
        selenium_base.wait_for_element(*login_page.user_name_input_box)
        driver.find_element(*login_page.user_name_input_box).send_keys(username)
        driver.find_element(*login_page.pwd_input_box).send_keys(pwd)
        driver.find_element(*login_page.login_button).click()

    def validate_the_login(self):
        selenium_base.wait_for_element(*login_page.logged_in_username)
        element= driver.find_element(*login_page.logged_in_username)
        inner_text = driver.execute_script("return arguments[0].innerText;", element)
        return inner_text
