import unittest
import requests

from base.api_base import APIBase


class TestAPISample(APIBase):

    def test_api(self):
        """
        This is the example to API test case.
        pass the arguments to the below method and get the response.
        :return:
        """
        request_type = requests.GET
        url = "http://api.open-notify.org/astros.json"
        allow_redirects = False
        cookies = None
        data = None
        params = None
        headers = None
        auth = None

        response = self.make_api_request(request_type, url, allow_redirects, cookies)
        print(response.status_code)

if __name__ == '__main__':
    unittest.main()
