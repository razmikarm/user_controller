from users import Admin, SimpleUser

USER_TYPE = {
    'admin': Admin,
    'simpleuser': SimpleUser
}

def get_by_role(role):
    return USER_TYPE[role]