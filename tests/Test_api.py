import unittest
import requests

from Resources import test_data
from apihelpers import api_helper
from apihelpers.api_helper import APIHelper
from base.api_base import APIBase


class TestAPISample(APIBase):

    @classmethod
    def setUpClass(cls):
        global api_helper
        api_helper = APIHelper()

    def test_api_status(self):
        """
        This is the example to API test case.
        pass the arguments to the below method and get the response.
        :return:
        """

        response = api_helper.api_GET_method(test_data.GET_request_type, test_data.url,
                                             test_data.allow_redirects, test_data.cookies)
        assert response.status_code == 200
        print(response.json())


if __name__ == '__main__':
    unittest.main()
