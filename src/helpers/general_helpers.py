import random
import string
import logging as logger

def generate_random_email_and_password(domain = None, email_prefix = None):
    domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testUser'
    email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=email_string_length))
    random_email = email_prefix + '_' + random_string + '@' + domain
    logger.info(f'Generated random email: {random_email}.')

    password_length = 20
    random_password = ''.join(random.choices(string.ascii_letters, k=password_length))
    logger.info(f'Generated random password: {random_password}.')

    random_info = {"email": random_email, "password": random_password}
    return random_info

