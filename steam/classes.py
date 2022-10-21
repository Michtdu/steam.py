
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


class ConfirmLogin:
    def __init__(self, auth_request):
        print(auth_request)
        self.__client_id = auth_request["client_id"]
        self.__request_id = auth_request["request_id"]
        self.__steam_id = auth_request["steamid"]

        self.confirmation_types = []
        for allowed_confirm in auth_request["allowed_confirmations"]: self.confirmation_types.append(allowed_confirm["confirmation_type"])

        self.is_confirmed = False
        self.allows_code = False
        self.allows_confirm = False

        if self.confirmation_types == [1]: self.is_confirmed = True
        if 2 in self.confirmation_types or 3 in self.confirmation_types: self.allows_code = True
        if 4 in self.confirmation_types or 5 in self.confirmation_types: self.allows_confirm = True

    def login(self, code=None):
        if code is None and not (self.is_confirmed or self.allows_confirm): raise Exception("Expected login code if account does not support mobile/email confirmation.")



