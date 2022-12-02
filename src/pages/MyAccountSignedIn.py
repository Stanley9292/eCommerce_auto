from src.locators.MyAccountSignedInLocators import MyAccountSignedInLocator
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url
import logging as logger

class MyAccountSignedIn(MyAccountSignedInLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.seleniumExtended.wait_until_element_is_visible(self.leftNavBarLogoutBtn)