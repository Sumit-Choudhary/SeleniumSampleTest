from Resources.Locators import LoginPageLocators as login_page
from base.selenium_base import SeleniumBase
from selenium.webdriver.common.keys import Keys


class SearchAndResultPage():
    def __init__(self):
        global driver, selenium_base
        selenium_base = SeleniumBase()
        driver = selenium_base.get_driver()

    def search_for_products(self, desired_search_item):
        search_box = driver.find_element(*login_page.search_box)
        selenium_base.wait_for_element(search_box)
        search_box.send_keys(desired_search_item)
        search_box.send_keys(Keys.ENTER)

    def select_lowest_priced_item(self):
        selenium_base.wait_for_element(driver.find_element(*login_page.first_item))
        driver.find_element(*login_page.first_item).click()

