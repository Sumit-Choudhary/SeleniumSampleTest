from selenium import webdriver
import unittest
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.config import *


class SeleniumBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = SeleniumBase().get_webdriver_instance()

    def get_driver(self):
        return driver

    def get_webdriver_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        # baseURL = "http://community.cty-dev.fidorfzco.com/"
        if browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            # Set chrome driver
            driver_location = webdriver_path
            os.environ["webdriver.chrome.driver"] = driver_location

            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            driver = webdriver.Chrome(driver_location, options=options)
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(1)
        return driver

    def wait_for_element(self, *locator, timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(driver, timeout=timeout,
                             poll_frequency=poll_frequency)
        wait.until(EC.presence_of_element_located(locator), "Max timeout reached. Element not found" + str(locator))

    def refresh_page(self):
        driver.refresh()

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()
