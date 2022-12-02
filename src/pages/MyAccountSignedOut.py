from src.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url
import logging as logger

class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f'Going to: {my_account_url}')
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.seleniumExtended.wait_and_input_text(self.usernameInput, username)

    def input_login_password(self, password):
        self.seleniumExtended.wait_and_input_text(self.passwordInput, password)

    def click_login_button(self):
        self.seleniumExtended.wait_and_click(self.loginBtn)

    def wait_until_error_displayed(self, expected_error):
        self.seleniumExtended.wait_until_element_contains_text(self.errorText, expected_error)

    def input_register_username(self, username):
        self.seleniumExtended.wait_and_input_text(self.registerEmailInput, username)

    def input_register_password(self, password):
        self.seleniumExtended.wait_and_input_text(self.registerPasswordInput, password)

    def click_register_button(self):
        self.seleniumExtended.wait_and_click(self.registerBtn)
