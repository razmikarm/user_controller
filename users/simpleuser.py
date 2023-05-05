from users import User

class SimpleUser(User):
    
    def __init__(self, username, email, full_name, password):
        self._username = username
        self._email = email
        self._full_name = full_name
        self.__password = password
        self._role = 'simpleuser'

    @property
    def password(self):
        return self.__password
    
    @property
    def email(self):
        return self._email
    
    @property
    def username(self):
        return self._username
    
    @property
    def full_name(self):
        return self._full_name
    
    @property
    def role(self):
        return self._role
    
    def update_password(self, old, new):
        if old == self.password:
            self.__password = new
        else:
            raise Exception("Old password is incorrect")
    
    def update_email(self, new):
        self._email = new
