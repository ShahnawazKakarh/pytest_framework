import allure
from jwt import encode


@allure.step
def generate_jwt_sh(company):
    """
    pop secret key from data and generate signed access token with secret key
    :param payload:
    :param secret_key:
    :return: signed jwt
    """

    # company configurations from database

    company_api_details = get_company_api_configuration_data(company)
    assert company_api_details, "Such Company Configurations are not found. Configure company" '{}'.format(company)

    api_token = company_api_details.get('api_token')
    secret_key = company_api_details.get('secret_key')

    return {'Authorization': 'Bearer ' + (encode(
        {
            "api_token": api_token
        },
        secret_key,
        algorithm='HS256'
    ).decode())}


@allure.step
def generate_jwt_with_session(company):
    """
    pop secret key from data and generate signed access token with secret key
    :param email_string:
    :return: signed jwt
    """
    data = {
        "header": generate_jwt_sh(company),
    }
    return data
