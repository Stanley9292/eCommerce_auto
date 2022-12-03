from src.locators.HomePageLocator import HomePageLocator
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url
import logging as logger

class HomePage(HomePageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def navigate_to_homepage(self):
        self.seleniumExtended.wait_and_click(self.homeBtn)

    def go_to_homepage(self):
        base_url = get_base_url()
        my_account_url = base_url
        logger.info(f'Going to: {my_account_url}')
        self.driver.get(my_account_url)

    def add_fourth_item_to_cart(self):
        self.seleniumExtended.wait_and_click(self.fourthItemAddToCartBtn)

    def add_first_item_to_cart(self):
        self.seleniumExtended.wait_and_click(self.allItemsAddToCartBtns)