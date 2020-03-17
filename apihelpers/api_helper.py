import logging
from base.api_base import APIBase

class APIHelper():

    """
    Helper method with various methods to assist API testing along with logging
    """
    def api_GET_method(self, request_type, url, allow_redirects=None, cookies=None, data=None, params=None,
                       headers=None, auth=None):
        """
        This method is used to validate a GET request
        :return:
        """
        logging.info('Starting GET request from the Helper method for ' + url)
        response = APIBase.make_api_request(request_type, url, allow_redirects, cookies)
        logging.info('Finished making request')
        if response.status_code != 200:
            logging.warning('Request failed with status code' + response.status_code)
        logging.info(response.status_code)
        logging.info('Request jason value is as follows' + response.json())
        return response