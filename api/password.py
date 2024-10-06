import os
import htpasswd

from api.auth import CONFIG_PATH

CONFIG_PATH = f'{str(os.path.dirname(os.path.realpath(__file__)))[:-3]}'

# https://github.com/thesharp/htpasswd

class Password:
    @staticmethod
    def change_password(data):
        with htpasswd.Basic(f'{CONFIG_PATH}config/.htpasswd') as userdb:
            try:
                userdb.change_password(data['user'], data['password'])
            except htpasswd.basic.UserNotExists:
                return False
        return Password.get_users()

    @staticmethod
    def add_user(data):
        with htpasswd.Basic(f'{CONFIG_PATH}config/.htpasswd') as userdb:
            try:
                userdb.add(data['user'], data['password'])
            except htpasswd.basic.UserExists:
                return False
        return Password.get_users()

    @staticmethod
    def delete_user(data):
        with htpasswd.Basic(f'{CONFIG_PATH}config/.htpasswd') as userdb:
            try:
                userdb.pop(data['user'])
            except htpasswd.basic.UserNotExists:
                return False
        return Password.get_users()

    @staticmethod
    def get_users():
        with htpasswd.Basic(f'{CONFIG_PATH}config/.htpasswd') as userdb:
            try:
                return userdb.users
            except Exception:
                return []
