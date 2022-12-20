from selenium.webdriver.common.by import By

class OrderReceivedPageLocator:
    pageMainHeader = (By.CSS_SELECTOR, 'h1.entry-title')
    orderNumberText = (By.CSS_SELECTOR, 'li.order strong')