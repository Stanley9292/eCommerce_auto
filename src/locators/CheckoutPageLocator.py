from selenium.webdriver.common.by import By

class CheckoutPageLocator:
    firstNameInput = (By.ID, 'billing_first_name')
    lastNameInput = (By.ID, 'billing_last_name')
    companyNameInput = (By.ID, 'billing_company')
    streetAddress1Input = (By.ID, 'billing_address_1')
    streetAddress2Input = (By.ID, 'billing_address_2')
    townInput = (By.ID, 'billing_city')
    zipCodeInput = (By.ID, 'billing_postcode')
    phoneInput = (By.ID, 'billing_phone')
    emailAddressInput = (By.ID, 'billing_email')
    placeOrderBtn = (By.ID, 'place_order')
    localPickUpRadioBtn = (By.ID, 'shipping_method_0_local_pickup3')