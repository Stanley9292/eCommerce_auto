from selenium.webdriver.common.by import By

class HomePageLocator:
    homeBtn = (By.XPATH, '(//a[contains(text(), "Home")])[1]')