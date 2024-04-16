from userrepository import user_repository as userrepository
from userrepository import User
from profilerepository import profile_repository as profilerepository
from profilerepository import Profile

class FinanceService:
    def __init__(self, users=userrepository, profiles=profilerepository):
        self._users = users
        self._user = None
        self._profiles = profiles

    def login(self, username, password):
        user = self._users.find_username(username)

        if not user or user.password != password:
            return None

        self._user = user
        return user

    def register(self, username, password):
        username_exists = self._users.find_username(username)
        if username_exists:
            return False
        new_user = self._users.create_new_user(User(username, password))

        self._user = new_user
        return new_user

    def create_profile(self, profile_name):
        new_profile = self._profiles.create_new_profile(Profile(profile_name))
        
        
        return new_profile
    
    def return_profiles(self, username):
        user = self._users.find_username(username)
        
        return self._profiles.find_all_with_user(user.username)