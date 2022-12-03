from src.locators.CartPageLocator import CartPageLocator
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url
import logging as logger

class CartPage(CartPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        base_url = get_base_url()
        my_account_url = base_url
        logger.info(f'Going to: {my_account_url}')
        self.driver.get(my_account_url)

    def add_item_to_cart(self):
        self.seleniumExtended.wait_and_click(self.fourthItemAddToCartBtn)