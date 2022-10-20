
# for internal use
class RequestInfo:
    def __init__(self, host, path, post=False):
        self.url = host + path
        self.post = post


# small classes the user will interact with
class GlobalStatistics:
    def __init__(self, statistics_dict):
        self.online = statistics_dict["users_online"]
        self.ingame = statistics_dict["users_ingame"]


class User:
    def __init__(self, user_dict):
        self.username = user_dict["persona_name"]
        self.avatar_url = user_dict["avatar_url"]

        self.id = user_dict["steamid"]
        self.account_id = user_dict["accountid"]
        self.url_username = user_dict["profile_url"]

        self.city = user_dict["city"]
        self.state = user_dict["state"]
        self.country = user_dict["country"]
        self.real_name = user_dict["real_name"]
