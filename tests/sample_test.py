from base.selenium_base import SeleniumBase
from base.api_base import APIBase
from pages.login_popup_page import LoginPopupPage


class TestFlipkartLogin(SeleniumBase, APIBase):
    """Below is the @BeforeClass method. This can be used if u want to perform any action everytime before Class"""

    @classmethod
    def setUpClass(cls):
        global login_page
        super().setUpClass()
        login_page = LoginPopupPage()

    """Below is the @BeforeTest method. This can be used if u want to perform any action everytime before method"""

    # def setUp(self):
    #     pass

    def test_login(self):
        """
        This is testcase 1
        :return:
        """
        login_page.load_flipkart("https://www.flipkart.com")
        login_page.login_to_account("abc@abc.com", "abc")
        self.assertEqual(1, 1, 'The login did not match')

    def test_navigate_to_page(self):
        """
        This is testcase 2
        :return:
        """
        pass

    def test_api(self):
        """
        This is the example to API test case.
        pass the arguments to the below method and get the response.
        :return:
        """
        resp = self.make_api_request("", "", "", "")
