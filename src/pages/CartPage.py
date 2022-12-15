from src.locators.CartPageLocator import CartPageLocator
from src.SeleniumExtended import SeleniumExtended
from src.locators.CartPageLocator import CartPageLocator

class CartPage(CartPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def go_to_cart_Page(self):
        pass

    def get_all_product_names_in_cart(self):
        product_name_elements = self.seleniumExtended.wait_and_get_elements(self.allProductNamesText)
        product_names = [i.text for i in product_name_elements]
        return product_names

    def input_coupon(self, coupon_code):
        self.seleniumExtended.wait_and_input_text(self.couponFieldInput, coupon_code)

    def click_apply_coupon(self):
        self.seleniumExtended.wait_and_click(self.applyCouponBtn)

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()

    def get_displayed_message(self):
        text = self.seleniumExtended.wait_and_get_text(self.couponMessageAlert)
        return text
