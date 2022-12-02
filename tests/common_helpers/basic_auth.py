from base64 import b64encode

import allure

username = 'qlzfqghpjhgfrmzg'
password = 'k$V}B*(6DQWuytkLH?4<rj3uGF;[~t>q'


@allure.step
def basic_auth_header():
    return {'Authorization': 'Basic {}'.format(
        (b64encode("{}:{}".format(username, password).encode('utf-8'))).decode("ascii"))}
