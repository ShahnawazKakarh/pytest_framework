"""
Author: Shahnawaz Khan
This file house validation tests for Sign Up API
"""

import pytest

from common_helpers.api_request_data.sign_up_data import data_for_sign_up_api_call
from common_helpers.api_request_helper import call_with
from common_helpers.basic_auth import basic_auth_header
from settings.settings import SIGNUP_END_POINT


@pytest.mark.usefixtures()
class TestSignUpApi(object):
    """
    Test User Sign Up Api
    """

    @pytest.fixture(scope='class')
    def user(self):
        return data_for_sign_up_api_call()

    @pytest.fixture(scope='class')
    def header(self):
        return basic_auth_header()

    @pytest.mark.ent_company
    def test_user_signup_and_validate_data(self, user, header):
        """
        Test the sign-up endpoint with new email.
        """

        # API CALL
        response_data = call_with(SIGNUP_END_POINT, user, header)
        assert response_data.get('http_response') == 422
        assert response_data.get('message') == "A customer with this email address exists."
