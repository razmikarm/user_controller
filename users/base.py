from abc import ABC, abstractmethod

class User(ABC):

    @property
    @abstractmethod
    def full_name(self): pass    

    @property
    @abstractmethod
    def email(self): pass
    
    @property
    @abstractmethod
    def username(self): pass

    @property
    @abstractmethod
    def password(self): pass
        
    @abstractmethod
    def update_password(self): pass
    
    @abstractmethod
    def update_email(self): pass
