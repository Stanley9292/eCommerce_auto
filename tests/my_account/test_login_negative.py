
import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures('init_driver')
class TestLoginNegative():

    @pytest.mark.negative
    def test_login_non_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)

        # go to my account 
        my_account.go_to_my_account()
        # type username
        my_account.input_login_username('adafdae')
        # type password
        my_account.input_login_password('adafdae')
        # click login
        my_account.click_login_button()
        # verify error message
        expected_error = 'is not registered on this site. If you are unsure of your username, try your email address instead.'
        expected_error2 = ': The username '
        my_account.wait_until_error_displayed(expected_error)
        my_account.wait_until_error_displayed(expected_error2)
        # import pdb; pdb.set_trace()