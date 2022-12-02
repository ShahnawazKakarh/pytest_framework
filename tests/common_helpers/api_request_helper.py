import allure
import requests

from settings.settings import BASE_URL, PATH


@allure.step
def call_with(end_point, data, header):
    response = requests.post(BASE_URL + PATH + end_point, json=data, headers=header)
    if response.status_code in [200, 201, 422]:
        return response.json()
    else:
        print(response.json())
        assert False, 'Critical: API failure with response code {}'.format(response.status_code)
