

import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage
from src.pages.Header import Header
from src.pages.CheckoutPage import CheckoutPage
from src.pages.OrderReceivedPage import OrderReceivedPage
from src.helpers.general_helpers import generate_random_email_and_password
from src.configs.generic_configs import GenericConfigs
from src.helpers.database_helpers import get_order_from_db_by_order_nr
import time
import os

@pytest.mark.e2e
class TestRegisterNewUser:

    @pytest.mark.usefixtures('init_driver')
    def test_end_to_end_checkout_guest_user(self):

        myAccountSignedOut = MyAccountSignedOut(self.driver)
        homePage = HomePage(self.driver)
        cartPage = CartPage(self.driver)
        header = Header(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        orderReceivedPage = OrderReceivedPage(self.driver)
 
        myAccountSignedOut.go_to_my_account()
        random_email = generate_random_email_and_password()
        myAccountSignedOut.input_register_username(random_email['email'])
        myAccountSignedOut.input_register_password(random_email['password'])
        myAccountSignedOut.click_register_button()

        homePage.go_to_homepage()
        homePage.add_first_item_to_cart()
        # homePage.add_fourth_item_to_cart()

        header.wait_until_cart_item_count(1)
        header.click_on_cart_right_header()

        product_names = cartPage.get_all_product_names_in_cart()

        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        env = os.environ.get('ENV')
        if env == 'prod':
            cartPage.apply_coupon(GenericConfigs.FREE_COUPON_PROD)
        else:
            cartPage.apply_coupon(GenericConfigs.FREE_COUPON_TEST)

        expected_message = 'Coupon code applied successfully.'
        actual_message = cartPage.get_displayed_message()
        assert expected_message == actual_message , f"Unexpected message when applying coupon."

        cartPage.click_checkout_button()
        checkoutPage.fill_in_billing_info()

        if env == 'prod':
            checkoutPage.click_local_pick_up()
        checkoutPage.click_place_order()

        orderReceivedPage.verify_order_received_page_loaded()

        order_nr = orderReceivedPage.get_order_number()
        print('********')
        print(order_nr)
        print('********')

        db_order = get_order_from_db_by_order_nr(order_nr)
        assert db_order, f"Entry not found in DB for order {order_nr}." 

        # import pdb; pdb.set_trace()