from src.locators.CheckoutPageLocator import CheckoutPageLocator
from src.SeleniumExtended import SeleniumExtended
from src.helpers.general_helpers import generate_random_email_and_password

class CheckoutPage(CheckoutPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.seleniumExtended = SeleniumExtended(self.driver)

    def input_billing_first_name(self, first_name = None):
        first_name = first_name if first_name else 'AutomationFname'
        self.seleniumExtended.wait_and_input_text(self.firstNameInput, first_name)

    def input_billing_last_name(self, last_name = None):
        last_name = last_name if last_name else 'AutomationLname'
        self.seleniumExtended.wait_and_input_text(self.lastNameInput, last_name)

    def input_billing_street_address_1(self, address = None):
        address = address if address else '123 Main St.'
        self.seleniumExtended.wait_and_input_text(self.streetAddress1Input, address)

    def input_billing_street_address_2(self, address = None):
        address = address if address else '112321 Main St.'
        self.seleniumExtended.wait_and_input_text(self.streetAddress2Input, address)
    
    def input_billing_city(self, city = None):
        city = city if city else 'Bucharest'
        self.seleniumExtended.wait_and_input_text(self.townInput, city)

    def input_billing_zipCode(self, zipCode = None):
        zipCode = zipCode if zipCode else '12345'
        self.seleniumExtended.wait_and_input_text(self.zipCodeInput, zipCode)

    def input_billing_phone(self, phone = None):
        phone = phone if phone else '074353234215'
        self.seleniumExtended.wait_and_input_text(self.phoneInput, phone)

    def input_billing_email(self, email = None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email'] 
        self.seleniumExtended.wait_and_input_text(self.emailAddressInput, email)

    def fill_in_billing_info(self, f_name=None, l_name=None, street1=None, street2=None, city=None, zipCode=None, phone=None, email = None):
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address_1(address=street1)
        self.input_billing_street_address_2(address=street2)
        self.input_billing_city(city=city)
        self.input_billing_zipCode(zipCode=zipCode)
        self.input_billing_phone(phone=phone)
        self.input_billing_email(email=email)