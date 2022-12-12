from selenium.webdriver.common.by import By

class HeaderLocators:
    cartHeaderRightBtn = (By.ID, 'site-header-cart')
    # this also works well -> itemsCountText = ul#site-header-cart span.count
    itemsCountText = (By.CSS_SELECTOR, 'a[class="cart-contents"] span[class="count"]')

