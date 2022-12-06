from SeleniumExtended import SeleniumExtended

class Header:
    
    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)
