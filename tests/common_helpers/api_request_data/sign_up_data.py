import allure
from common_helpers.dict_helpers_sh import get_me_device_key_and_id
from faker import Faker

device_key = get_me_device_key_and_id()
fake = Faker()

password = "testQa@123"


def random_email():
    fake = Faker()
    email = fake.email()
    return 'testqa_autotest{email}'.format(email=email)


# Sign Up Data for Entertainer
@allure.step
def data_for_sign_up_api_call():
    email_random = random_email

    data = {
        "company": "",
        "email": email_random,
        "password": password,
        "confirm_password": password,
        'firstname': "Automation",
        'lastname': fake.last_name(),
        'gender': 'MALE',
        'device': device_key
    }

    return data
