from src.locators.OrderReceivedPageLocator import OrderReceivedPageLocator
from src.SeleniumExtended import SeleniumExtended

class OrderReceivedPage(OrderReceivedPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.seleniumExtended.wait_until_element_contains_text(self.pageMainHeader, 'Order received')

    