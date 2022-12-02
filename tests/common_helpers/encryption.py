import base64
import json

from Crypto.Cipher import AES

encryption_mode = AES.MODE_CBC
encryption_key = "18b8c9ef4jhgty7890k56ab0cb2b71cb"
encryption_salt_iv = "18buio8767hg8126"


def pkcs7_padding(b_string, k=16):
    """
    Pad an input byte string according to PKCS#7
    """
    length = len(b_string)
    val = k - (length % k)
    return b_string + bytearray([val] * val)


def encrypt_data(data_to_encrypt, key=encryption_key, salt=encryption_salt_iv, mode=encryption_mode):
    """
    Returns data after encrypting via AES using provided key, salt & mode
    :param int mode: Decryption mode
    :param str key: Decryption key
    :param str salt: 16 bit salt
    :param bytes data_to_encrypt: data to encrypt
    :returns bytes,str: encrypted data or empty string
    """
    try:
        data_to_encrypt = json.dumps(data_to_encrypt).encode('utf8')
        data_to_encrypt = pkcs7_padding(data_to_encrypt, 16)
        aes = AES.new(key, mode=mode, IV=salt)
        encrypted_str = aes.encrypt(data_to_encrypt)
        params = base64.b64encode(encrypted_str).decode()
        print("params: {}".format(params))
        return {'params': params.replace("+", "-").replace("/", "_").replace("=", ",")}
    except Exception as e:
        print(e)
        return ""
