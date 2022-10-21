
class LoginTypes:
    none = 1
    email_code = 2
    mobile_code = 3
    mobile_confirm = 4
    email_confirm = 5

    def __getitem__(self, item):
        enum = [
            "none",
            "email_code",
            "mobile_code",
            "mobile_confirm",
            "email_confirm"
        ]
        return enum[item - 1]

