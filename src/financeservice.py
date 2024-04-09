from userrepository import user_repository as userrepository
from userrepository import User

class FinanceService:
    def __init__(self, users=userrepository):
        self._users = users
        self._user = None
        
    def login(self, username, password):
        user = self._users.find_username(username)
        
        if not user or user.password != password:
            return None

        self._user = user
        return user
    
    def register(self, username, password):
        newUser = self._users.create_new_user(User(username, password))
        
        self._user = newUser
        return newUser