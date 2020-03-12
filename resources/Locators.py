from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_input_box = (By.CSS_SELECTOR, "[class='_2zrpKA _1dBPDZ']")
    pwd_input_box = (By.CSS_SELECTOR, "[class='_2zrpKA _3v41xv _1dBPDZ']")
    login_button = (By.CSS_SELECTOR, "[class='_2AkmmA _1LctnI _7UHT_c']")
