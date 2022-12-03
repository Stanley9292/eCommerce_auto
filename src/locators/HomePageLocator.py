from selenium.webdriver.common.by import By

class HomePageLocator:
    homeBtn = (By.XPATH, '(//a[contains(text(), "Home")])[1]')
    fourthItemAddToCartBtn = (By.CSS_SELECTOR, 'a[data-product_id="16"]')
    allItemsAddToCartBtns = (By.CSS_SELECTOR, 'a.add_to_cart_button')