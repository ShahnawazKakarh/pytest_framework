"""
Helpers methods for Shahnawaz Khan
Author Shahnawaz
Not to be used in actual project this file should be excluded from commits
"""
import json
import random
import re
import string
from datetime import datetime

from faker import Faker


def default(o):
    import datetime
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


def write_to_file(base_url, params):
    filename = "params-" + datetime.now().strftime("%Y-%m-%d") + ".log"
    f = open(filename, "a+")
    params = json.dumps(params, sort_keys=True, indent=4, default=default)
    time_stamp = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    f.write(str(time_stamp + '\n' + base_url) + '\n' + params + '\n''\n')
    f.close()


def dict_to_json_and_prettify(my_dict):
    return json.dumps(my_dict, sort_keys=True, indent=4, default=default)


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def random_numbers(string_length=8):
    """Generate a random number of fixed length """
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(string_length))


def long_random_numbers(string_length=12):
    """Generate a random number of fixed length """
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(string_length))


def random_string_number(string_length=4):
    """Generate a random string of hexdigits fixed length """
    number = string.digits
    return ''.join(random.choice(number) for i in range(string_length))


def random_email():
    fake = Faker()
    email = fake.email()
    return 'testqa_autotest_{email}'.format(email=email)


def get_me_device_key_and_id():
    first_random = random_numbers()
    second_random = random_string_number()
    third_random = random_string_number()
    fourth_random = random_string_number()

    device_key = 'automation-{first_random}-{second_random}-{third_random}-{fourth_random}'.format(
        first_random=first_random, second_random=second_random, third_random=third_random, fourth_random=fourth_random)

    return device_key


def valid_email(email):
    pattern = r"\"?([-a-zA-Z0-9+_.`?{}]+@[-a-zA-Z0-9+_.`?{}]+\.\w+)\"?"
    pattern = re.compile(pattern)
    if re.match(pattern, email):
        return True
    else:
        return False
