import json
import logging

from base.api_base import APIBase


class APIHelper:
    api_base = APIBase()
    """
    Helper method with various methods to assist API testing along with logging
    """
    logging.basicConfig(level=logging.DEBUG)

    def api_GET_method(self, request_type, url, allow_redirects=None, cookies=None, data=None, params=None,
                       headers=None, auth=None):
        """
        This method is used to validate a GET request
        :return:
        """
        logging.info('Starting GET request from the Helper method for ' + url)
        response = APIBase.make_api_request(self, request_type, url, allow_redirects, cookies)
        logging.info('Finished making request')
        if response.status_code != 200:
            logging.warning("Request failed with status code {statuscode}.".format(statuscode=response.status_code))
        logging.info("Status code received as {statuscode}".format(statuscode=response.status_code))
        return response

    def jprint(self, json_obj):
        """
        Create a formatted string of the Python JSON object which is passed as parameter
        :return:
        """
        formatted_json_text = json.dumps(json_obj, sort_keys=True, indent=4)
        return formatted_json_text

