import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.pages.MyAccountSignedIn import MyAccountSignedIn
from src.helpers.general_helpers import generate_random_email_and_password

@pytest.mark.register
class TestRegisterNewUser:

    @pytest.mark.usefixtures('init_driver')
    def test_register_valid_new_user(self):
        myAccountSignedOut = MyAccountSignedOut(self.driver)
        myAccountSignedIn = MyAccountSignedIn(self.driver)
 
        myAccountSignedOut.go_to_my_account()
       
        random_email = generate_random_email_and_password()
        myAccountSignedOut.input_register_username(random_email['email'])
        
        myAccountSignedOut.input_register_password(random_email['password'])
        myAccountSignedOut.click_register_button()

        myAccountSignedIn.verify_user_is_signed_in()

        # import pdb; pdb.set_trace()