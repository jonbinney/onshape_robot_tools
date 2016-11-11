import base64
import datetime
import json
import hashlib
import hmac
import os.path
import random
import requests
import urllib
import yaml

class OnshapeClient:
    def __init__(self):
        config_file_path = os.path.expanduser('~/.config/onshape_robot_tools/config.yml')
        with open(config_file_path, 'r') as config_file:
            config_data = yaml.load(config_file)
        self._api_access_key = config_data['api_access_key']
        self._api_secret_key = config_data['api_secret_key']
        self._base_url = 'https://cad.onshape.com'

    def _create_request_headers(self, method, path, query_dict={}):
        """
        method - 'POST' or 'GET'
        path - path to REST endpoint, e.g. /api/documents
        """

        date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        query_str = urllib.urlencode(query_dict)
        nonce = ''.join([str(random.randint(0, 9)) for i in range(16)])
        content_type = 'application/json'

        hmac_str = ''.join(['{}\n'.format(s) for s in method, nonce, date, content_type, path,
            query_str]).lower().encode('utf-8')

        signature = base64.b64encode(
            hmac.new(self._api_secret_key, hmac_str, digestmod=hashlib.sha256).digest())
        auth = 'On {}:HmacSHA256:{}'.format(self._api_access_key, signature.decode('utf-8'))

        headers = {
            'Content-Type': content_type,
            'Accept': content_type,
            'User-Agent': 'Robot Tools',
            'Date': date,
            'On-Nonce': nonce,
            'Authorization': auth,
        }

        return headers

    def make_request(self, method, path, query_dict={}):
        """
        method - 'POST' or 'GET'
        path - path to REST endpoint
        query - query params as dictionary
        body - body of message to send
        """
        headers = self._create_request_headers(method, path, query_dict)
        url = '{}{}?{}'.format(self._base_url, path, urllib.urlencode(query_dict))
        return requests.request(method, url, headers=headers, data='', allow_redirects=False, stream=True)
