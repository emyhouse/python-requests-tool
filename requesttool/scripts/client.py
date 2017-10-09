# -*- coding: utf-8 -*-
import requests

class RequestClient(object):

    def __init__(self, url, token):
        self.url = url 
        self.token = token

    def get(self, api_addr, payload=None):
        """
        :param: payload 
            {'key1': 'value1', 'key2': 'value2'}
        """
        uri = "{0}{1}".format(self.url, api_addr)
        headers = {'authorization': self.token}
        if payload is None:
            r = requests.get(uri)
        else:
            r = requests.get(uri, params=payload, headers=headers)
        result = r.json()
        return result
