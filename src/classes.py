
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
