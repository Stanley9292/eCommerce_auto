import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.helpers.general_helpers import generate_random_email_and_password

@pytest.mark.register
class TestRegisterNewUser:

    @pytest.mark.usefixtures('init_driver')
    def test_register_valid_new_user(self):
        my_account = MyAccountSignedOut(self.driver)
 
        my_account.go_to_my_account()
       
        random_email = generate_random_email_and_password()
        my_account.input_register_username(random_email['email'])
        
        my_account.input_register_password(random_email['password'])
        
        my_account.click_register_button()
        

        import pdb; pdb.set_trace()