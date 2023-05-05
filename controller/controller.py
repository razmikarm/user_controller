from os import path
from csv import DictReader
from users import Admin, SimpleUser
from utils import get_by_role

class Controller:

    def __init__(self, filename):
        self._filename = filename
        self._data = None
        self._users = []
        self._read_csv()

    def _read_csv(self):
        if not path.exists(self._filename):
            with open(self._filename, 'w') as _: pass
        with open(self._filename) as file:
            self._data = list(DictReader(file))
        self._generate_users()

    def _generate_users(self):
        for user_data in self.data:
            user_data = user_data.copy()
            role = user_data.pop('role')
            user_class = get_by_role(role)
            user = user_class(**user_data)
            self._users.append(user)

    @property
    def data(self):
        return self._data

    @property
    def users(self):
        return self._users

    def login(self):
        pass

    def add_user(self):
        pass

    def get_user(self):
        pass

    def del_user(self):
        pass
