from selenium.webdriver.common.by import By

class CartPageLocator:
    allProductNamesText = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    couponFieldInput = (By.ID, 'coupon_code')
    applyCouponBtn = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')