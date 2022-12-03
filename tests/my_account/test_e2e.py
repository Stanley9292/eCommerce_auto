

import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.pages.MyAccountSignedIn import MyAccountSignedIn
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage
from src.helpers.general_helpers import generate_random_email_and_password

@pytest.mark.e2e
class TestRegisterNewUser:

    @pytest.mark.usefixtures('init_driver')
    def test_end_to_end_checkout_guest_user(self):
        # go to home page
        # add 1 item to cart
        # go to cart
        # apply free cupon
        # select free shipping
        # click on checkout
        # fill form
        # click on place order
        # verify order is received
        # verify order is recorded in db


        myAccountSignedOut = MyAccountSignedOut(self.driver)
        # myAccountSignedIn = MyAccountSignedIn(self.driver)
        homePage = HomePage(self.driver)
        cartPage = CartPage(self.driver)
 
        myAccountSignedOut.go_to_my_account()
        random_email = generate_random_email_and_password()
        myAccountSignedOut.input_register_username(random_email['email'])
        myAccountSignedOut.input_register_password(random_email['password'])
        myAccountSignedOut.click_register_button()

        homePage.go_to_homepage()
        homePage.add_first_item_to_cart()

        import pdb; pdb.set_trace()