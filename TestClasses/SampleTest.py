from PageClasses import loginPopUp
import unittest
from selenium import webdriver


def login():
    v = loginPopUp.flipkartMainLoginPopOver(webdriver.Firefox())
    v.loadFlipKart()
    v.loginToFlipKart('8939667714', 'cometome')


class ValidateFlipKartLogin(unittest.TestCase):
    def testlogin(self):
        login()
        self.assertEqual(1==1)

    if __name__ == '__main__':
        unittest.main()
