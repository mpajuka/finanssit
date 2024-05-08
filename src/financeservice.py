from userrepository import user_repository as userrepository
from userrepository import User
from profilerepository import profile_repository as profilerepository
from profilerepository import Profile
from transactionrepository import transaction_repository as transactionrepository
from transactionrepository import Transaction


class FinanceService:
    def __init__(self, users=userrepository, profiles=profilerepository,
                 transactions=transactionrepository):
        self._users = users
        self._user = None
        self._profiles = profiles
        self._transactions = transactions

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

    def create_profile(self, profile_name, username):
        new_profile = self._profiles.create_new_profile(
            Profile(profile_name, username))

        return new_profile

    def find_profile(self, profile_name):
        profile = self._profiles.find_profile(profile_name)

        return profile

    def return_profiles(self, username):
        return self._profiles.find_all_with_user(username)

    def create_transaction(self, name, amount, profile):
        if amount == "" or name == "":
            return False
        new_transaction = self._transactions.create_transaction(
            Transaction(name, amount, profile))

        return new_transaction

    def return_transactions(self, profile):
        return self._transactions.find_all_transactions_with_profile(profile)

    def return_profile_balance(self, profile):
        return self._transactions.sum_of_profile_transactions(profile)
