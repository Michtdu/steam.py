import requests
import rsa

from time import sleep
from base64 import b64encode

import private_enum as e
import classes as c


# noinspection PyTypeChecker
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

    def get_store_tags(self):
        request = self.__request(e.Requests.Store.get_tags)["tags"]
        tags = {}
        for tag in request: tags[tag["tagid"]] = tag["name"]
        return tags

    # supports a list of user ids or a single user id (Note that if len(user_id) > 200 you might have to wait a bit)
    def resolve_user(self, user_id):
        if type(user_id) == list:
            if len(user_id) > 200:
                split_user_ids = []
                while user_id: split_user_ids.append(user_id[:200]); user_id = user_id[200:]
                results = []
                for users in split_user_ids:
                    for user in self.resolve_user(users): results.append(user)

                return results

            else:
                unlisted = ""
                for _id in user_id: unlisted += _id + ','
                unlisted = unlisted[:-1]
                params = {"steamids": unlisted}
        else: params = {"steamids": user_id}
        request = self.__request(e.Requests.User.get_user, params)

        if len(request) > 1:
            result = []
            for user in request: result.append(c.User(user))
        else: result = c.User(request[0])

        return result
