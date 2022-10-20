import requests
import rsa

from time import sleep
from base64 import b64encode

import private_enum as e
import classes as c


class Session:
    def __init__(self):
        self.__session = requests.Session()

    def __request(self, request_info, params={}):
        try:
            if request_info.post: request = self.__session.post(request_info.url, params=params)
            else: request = self.__session.get(request_info.url, params=params)

        except requests.exceptions.ConnectionError: return self.__request(request_info, params)
        if request.status_code == 429: sleep(10); return self.__request(request_info, params)

        try: return request.json()
        except requests.exceptions.JSONDecodeError: return request.text

    def get_global_stats(self):
        return c.GlobalStatistics(self.__request(e.Requests.Miscellaneous.get_global_stats))


