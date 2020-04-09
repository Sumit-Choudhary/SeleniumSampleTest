import unittest

from Resources import test_data
from base.selenium_base import SeleniumBase
from pages.login_start_page import LoginAndStartPage
from pages.search_result_page import SearchAndResultPage


class TestFlipkartLogin(SeleniumBase):
    """Below is the @BeforeClass method. This can be used if u want to perform any action every time before Class"""

    @classmethod
    def setUpClass(cls):
        global login_page, search_result_page
        super().setUpClass()
        login_page = LoginAndStartPage()
        search_result_page = SearchAndResultPage()

    """Below is the @BeforeTest method. This can be used if u want to perform any action everytime before method"""

    # def setUp(self):
    #     pass

    def test_login(self):
        """
        This is testcase 1
        :return:
        """
        login_page.load_flipkart(test_data.marketurl)
        login_page.login_to_account(test_data.username, test_data.password)
        self.assertEqual(login_page.validate_the_login(), test_data.test_logged_in_user, 'The login did not match')

    def test_selection_lowest_priced_item(self):
        search_result_page.search_for_products(test_data.item_to_search)
        search_result_page.select_lowest_priced_item()

    def tearDown(self):
        login_page.logout()


if __name__ == '__main__':
    unittest.main()
