from base.selenium_base import SeleniumBase
from pages.login_popup_page import LoginPopupPage


class TestFlipkartLogin(SeleniumBase):
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
