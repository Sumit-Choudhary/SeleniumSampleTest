from selenium.webdriver.common.by import By
from selenium import webdriver

class flipkartMainLoginPopOver:
    URL = 'https://www.flipkart.com'

    def __init__(self, driver):
        self.driver = driver

    def loadFlipKart(self):
        self.driver.get(self.URL)

    def loginToFlipKart(self, usernamevalue, password):
        userNameInputBox = self.driver.find_element_by_css_selector("[class='_2zrpKA _1dBPDZ']")
        passwordInputBox = self.driver.find_element_by_css_selector("[class='_2zrpKA _3v41xv _1dBPDZ']")
        loginbutton = self.driver.find_element_by_css_selector("[class='_2AkmmA _1LctnI _7UHT_c']")

        userNameInputBox.send_keys(usernamevalue)
        passwordInputBox.send_keys(password)
        loginbutton.click()
