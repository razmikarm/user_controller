from os import path
from csv import DictReader
from users import Admin, SimpleUser
from utils import get_by_role
from utils import config

class Controller:

    def __init__(self, filename):
        self._filename = filename
        self._data = None
        self._users = []
        self._read_csv()
        self._current_user = None

    def _read_csv(self):
        if not path.exists(self._filename):
            with open(self._filename, 'w') as _: pass
            self.add_user('admin')
        with open(self._filename) as file:
            self._data = list(DictReader(file))
        self._generate_users()

    def _generate_users(self):
        for user_data in self.data:
            user_data = user_data.copy()
            role = user_data.pop('role')
            user_type = get_by_role(role)
            user = user_type(**user_data)
            self._users.append(user)

    @property
    def data(self):
        return self._data

    @property
    def users(self):
        return self._users

    def login(self):
        pass

    def add_user(self, role=None):
        all_roles = config.USER_TYPES.keys()
        if role == None:
            role = input("Enter role: ")
        if role not in all_roles:
            raise ValueError(f'There is no such user role: {role}')
        email = input("Enter email: ")
        self._validate_email(email)
        uname = input("Enter username: ")
        self._validate_username(uname)
        pwd = input("Enter password: ")
        fname = input("Enter full name: ")
        user_type = get_by_role(role)
        user = user_type(
            username=uname,
            password=pwd,
            email=email,
            full_name=fname,
        )
        self._users.append(user)

    def get_user(self):
        pass

    def del_user(self):
        pass

    def _validate_email(self, email):
        pass

    def _validate_username(self, username):
        pass
