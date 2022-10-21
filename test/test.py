import steam
from login_data import *

session = steam.Session()

user = session.login(username1, password1)
print(user)
