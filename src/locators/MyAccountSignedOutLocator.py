from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:
    usernameInput = (By.ID, 'username')
    passwordInput = (By.ID, 'password')
    loginBtn = (By.CSS_SELECTOR, 'button[value="Log in"]')
    errorText = (By.XPATH, '//ul[@class="woocommerce-error"]//li')
    registerEmailInput = (By.ID, 'reg_email')
    registerPasswordInput = (By.ID, 'reg_password')
    registerBtn = (By.CSS_SELECTOR, 'button[value="Register"]')