from users import Admin, SimpleUser
from utils import config

def get_by_role(role):
    return config.USER_TYPES[role]
