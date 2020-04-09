from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_input_box = (By.CSS_SELECTOR, "[class='_2zrpKA _1dBPDZ']")
    pwd_input_box = (By.CSS_SELECTOR, "[class='_2zrpKA _3v41xv _1dBPDZ']")
    login_button = (By.CSS_SELECTOR, "[class='_2AkmmA _1LctnI _7UHT_c']")
    logged_in_username = (By.CSS_SELECTOR, "div._3pNZKl > div:nth-child(3) ._2aUbKa")
    logout_button = (By.CSS_SELECTOR, "a._2k68Dy")
    search_box = (By.CSS_SELECTOR, "div.O8ZS_U>input,LM6RPg")
    sort_button_low_to_high= (By.CSS_SELECTOR, "div._1xHtJz.xufquN")
    first_item = (By.CSS_SELECTOR, "div._3O0U0u div.IIdQZO._1SSAGr a._3dqZjq")
