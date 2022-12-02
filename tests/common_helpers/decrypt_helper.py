import base64
import json

import allure
from Crypto.Cipher import AES


def pkcs7_un_padding(b_string):
    return b_string[0:-ord(b_string[-1])]


def decode_params(key, salt, mode, encoded_params, add_padding=True):
    """
    Decodes params
    :param int mode: Decryption mode
    :param str key: Decryption key
    :param str salt: 16 bit salt
    :param bytes encoded_params: Encoded params
    :rtype: dict
    """
    aes = AES.new(key, mode=mode, IV=salt)
    if add_padding:
        decrypted_str = aes.decrypt(encoded_params)
        decrypted_str = decrypted_str.decode(errors='ignore')
        decrypted_str = pkcs7_un_padding(decrypted_str)
    else:
        decrypted_str = aes.decrypt(encoded_params)
        decrypted_str = decrypted_str.decode(errors='ignore')
    return decrypted_str


@allure.step
def decrypt_response(response):
    """
    decrypt response of api
    :param response:
    :return decrypted_json:
    """
    key = "18b8c9ef473asdfj7864jljhab0cb2b71cb"
    salt = "18hjk87654fg2126"
    mode = 2
    param = base64.b64decode(response.text)
    decrypted_str = decode_params(key, salt, mode, param)
    return json.loads(decrypted_str)
