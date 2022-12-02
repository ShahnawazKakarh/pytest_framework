import allure
from common_helpers.dict_helpers_sh import get_me_device_key_and_id
from faker import Faker

device_key = get_me_device_key_and_id()
fake = Faker()

password = "testQa@123"


def random_email():
    fake = Faker()
    email = fake.email()
    return 'testqa_autotest_ent{email}'.format(email=email)


# Sign Up Data for Entertainer
@allure.step
def data_for_sign_up_api_call():
    email_random = random_email

    data = {
        "company": "",
        "__platform": "ios",
        "app_version": "6.23.01",
        "language": "en",
        "email": email_random,
        "password": password,
        "confirm_password": password,
        'firstname': "Automation",
        'lastname': fake.last_name(),
        'terms_acceptance': 1,
        "country_of_residence": "AE",
        'is_privacy_policy_accepted': 1,
        'os_version': "12.3.1",
        'gender': 'MALE',
        'device_os': 'ios',
        'device_model': 'iPhoneX',
        '__device_id': device_key,
        'is_user_agreement_accepted': 1,
    }

    return data
