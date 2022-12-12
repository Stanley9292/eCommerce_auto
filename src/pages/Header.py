from src.SeleniumExtended import SeleniumExtended
from src.locators.HeaderLocators import HeaderLocators

class Header(HeaderLocators):
    
    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def click_on_cart_right_header(self):
        self.seleniumExtended.wait_and_click(self.cartHeaderRightBtn)

    def wait_until_cart_item_count(self, count):
        if count == 1:
            expected_text = str(count) + ' item'
        else:
            expected_text = str(count) + ' items'
        
        self.seleniumExtended.wait_until_element_contains_text(self.itemsCountText, expected_text)
