from PageClasses import loginPopUp
import unittest
from selenium import webdriver

v = loginPopUp.flipkartMainLoginPopOver(webdriver.Firefox())
def login():

    v.loadFlipKart()
    v.loginToFlipKart('8939667714', 'cometome.23')


class ValidateFlipKartLogin(unittest.TestCase):
    def test_login(self):
        login()
        self.assertEqual(1 == 1)

    def teardown(self):
        v.closeTheBrowser()

if __name__ == '__main__':
    unittest.main()
