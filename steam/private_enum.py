from steam.classes import RequestInfo


class Hosts:
    api = "https://api.steampowered.com/"
    store = "https://store.steampowered.com/"
    community = "https://steamcommunity.com/"
    valve = "https://www.valvesoftware.com/"


class Requests:
    class Login:
        get_rsa = RequestInfo(Hosts.api, "IAuthenticationService/GetPasswordRSAPublicKey/v1/")
        session_request = RequestInfo(Hosts.api, "IAuthenticationService/BeginAuthSessionViaCredentials/v1/", True)
        get_refresh_token = RequestInfo(Hosts.api, "IAuthenticationService/PollAuthSessionStatus/v1/", True)

    class Miscellaneous:
        get_global_stats = RequestInfo(Hosts.valve, "about/stats/")

    class Store:
        get_tags = RequestInfo(Hosts.store, "actions/ajaxgetstoretags/")

    class User:
        get_user = RequestInfo(Hosts.community, "actions/ajaxresolveusers/")
