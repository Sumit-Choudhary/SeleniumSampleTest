import requests


class APIBase:

    def make_api_request(self, request_type, url, allow_redirects=None, cookies=None, data=None, params=None,
                         headers=None, auth=None):
        """
        This is a utility method to make any api request.
        :param request_type: GET/ POST /PUT ..
        :param url: URL of the API application
        :param allow_redirects: 
        :param cookies:
        :param data:
        :param params:
        :param headers:
        :param auth:
        :return: response
        """
        response = requests.request(request_type.value, url, allow_redirects=allow_redirects, cookies=cookies,
                                    data=data,
                                    params=params,
                                    headers=headers,
                                    auth=auth)
        return response
