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
        import pdb; pdb.set_trace()
        product_names = [i.text for i in product_name_elements]
        return product_names
