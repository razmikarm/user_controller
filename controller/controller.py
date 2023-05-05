from os import path
from csv import DictReader
from users import Admin, SimpleUser

class Controller:

    def __init__(self, filename):
        self._filename = filename
        self._data = None
        self._read_csv()

    def _read_csv(self):
        if not path.exists(self._filename):
            with open(self._filename, 'w') as _: pass
        with open(self._filename) as file:
            self._data = list(DictReader(file))

    @property
    def data(self):
        return self._data

    def login(self):
        pass

    def add_user(self):
        pass

    def get_user(self):
        pass

    def del_user(self):
        pass
