from repositories.userrepository import user_repository as userrepository
from repositories.userrepository import User
from repositories.profilerepository import profile_repository as profilerepository
from repositories.profilerepository import Profile
from repositories.transactionrepository import transaction_repository as transactionrepository
from repositories.transactionrepository import Transaction


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
        if username == "":
            return "Error: username must not be empty"

        if len(password) < 8:
            return """Error: password must contain at least\n 8 characters, 1 number
                        and\n1 special character"""

        if not any(c.isnumeric() for c in password):
            return "Error: password must contain at least\n1 number and 1 special character"

        if password.isalnum():
            return "Error: password must contain at least\n1 special character"

        username_exists = self._users.find_username(username)
        if username_exists:
            return "Error: username already exists"

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

    def create_transaction(self, name, amount_entry, profile, radio_value, date):
        if amount_entry == "" or name == "":
            return "Error: transaction name or amount missing"

        try:
            float(amount_entry)
        except ValueError:
            return "Error: amount must be a numeric value"

        if radio_value == "":
            return "Error: transaction type missing"

        if radio_value == "Expense":
            amount = -abs(float(amount_entry))
        else:
            amount = float(amount_entry)

        new_transaction = self._transactions.create_transaction(
            Transaction(name, amount, profile, date))

        return new_transaction

    def edit_transaction(self, name, amount_entry, profile, radio_value, transaction_id, date):
        if amount_entry == "" or name == "":
            return "Error: transaction name or amount missing"
        try:
            float(amount_entry)
        except ValueError:
            return "Error: amount must be a numeric value"

        if radio_value == "":
            return "Error: transaction type missing"

        if radio_value == "Expense":
            amount = -abs(float(amount_entry))
        else:
            amount = float(amount_entry)

        edit_transaction = self._transactions.edit_transaction(
            Transaction(name, amount, profile, date, transaction_id))

        return edit_transaction

    def remove_transaction(self, transaction_id):
        return self._transactions.remove_transaction(transaction_id)

    def get_transaction(self, transaction_id):
        return self._transactions.get_transaction(transaction_id)

    def return_transactions(self, profile):
        return self._transactions.find_all_transactions_with_profile(profile)

    def return_profile_balance(self, profile):
        return self._transactions.sum_of_profile_transactions(profile)
