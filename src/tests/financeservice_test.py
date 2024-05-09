import unittest
from financeservice import FinanceService
from userrepository import User
from profilerepository import Profile
from transactionrepository import Transaction

class TestFinanceService(unittest.TestCase):
    def setUp(self):
        self._app = FinanceService()
        self._user = None
        self._p = Profile("test", "kayttaja2")

    def test_user_does_not_exist(self):
        self._user = User("kayttaja1", "salasana1")
        self.assertEqual(
            self._app.login(self._user.username, self._user.password), None)

    def test_user_registration(self):
        self._user = User("kayttaja1", "salasana1")
        self.assertNotEqual(
            self._app.register(self._user.username, self._user.password), None)

    def test_user_exists(self):
        self._user = User("kayttaja2", "salasana2")
        self.assertNotEqual(
            self._app.register(self._user.username, self._user.password), None)
        self.assertNotEqual(
            self._app.login(self._user.username, self._user.password), None)

    def test_create_profile(self):
        u = User("kayttaja2", "salasana2")

        self._app.register(u.username, u.password)
        self._app.login(u.username, u.password)

        new_profile = self._app.create_profile(self._p.name, self._p.username)
        self.assertEqual(new_profile.id, 1)

    def test_find_profile(self):
        u = User("kayttaja2", "salasana2")

        self._app.register(u.username, u.password)
        self._app.login(u.username, u.password)

        get_profile = self._app.find_profile(self._p.name)
        self.assertEqual(self._p.name, get_profile.name)

    def test_return_profiles(self):
        self._app = FinanceService()
        u = User("kayttaja2", "salasana2")

        profiles = self._app.return_profiles(u.username)
        self.assertEqual(profiles[0].name, self._p.name)

    def test_create_transaction(self):
        p = Profile("test", "kayttaja2", 1)
        t = Transaction("Name", 100, p, "2024-01-01")
        new_transaction = self._app.create_transaction(t.name, t.amount, t.profile, "Expense",
                                                       t.date)
        self.assertEqual(new_transaction.id, 1)

    def test_get_transaction(self):
        p = Profile("test", "kayttaja2", 1)
        t = Transaction("Name", 100, p, "2024-01-01")
        new_transaction = self._app.create_transaction(t.name, t.amount, t.profile, "Expense",
                                                       t.date)

        get_transaction = self._app.get_transaction(new_transaction.id)
        self.assertEqual(get_transaction.id, new_transaction.id)


    def test_edit_transaction(self):
        p = Profile("test", "kayttaja2", 1)
        t = Transaction("Name", 200, p, "2024-01-01")
        get_transaction = self._app.get_transaction(1)
        self.assertEqual(get_transaction.amount, -100)
        self._app.edit_transaction(t.name, t.amount, t.profile, "Income",
                                                       get_transaction.id, t.date)
        get_transaction = self._app.get_transaction(1)
        self.assertEqual(get_transaction.amount, t.amount)


    def test_edit_transaction_fails_with_misinput(self):
        p = Profile("test", "kayttaja2", 1)
        t = Transaction("Name", "123.a", p, "2024-01-01")
        get_transaction = self._app.get_transaction(1)
        self.assertEqual(get_transaction.amount, 200)
        self._app.edit_transaction(t.name, t.amount, t.profile, "Income",
                                                       get_transaction.id, t.date)
        get_transaction = self._app.get_transaction(1)
        self.assertNotEqual(get_transaction.amount, t.amount)


    def test_remove_transaction(self):
        get_transaction = self._app.get_transaction(1)
        self.assertIsInstance(get_transaction, Transaction)
        self._app.remove_transaction(get_transaction.id)
        get_transaction = self._app.get_transaction(1)
        self.assertNotIsInstance(get_transaction, Transaction)


    def test_return_transactions(self):
        p = Profile("test", "kayttaja2", 1)
        transactions = self._app.return_transactions(p)
        self.assertEqual(transactions[0].profile, 1)


    def test_return_profile_balance(self):
        p = Profile("test", "kayttaja2", 1)
        profile_balance = self._app.return_profile_balance(p)
        self.assertEqual(profile_balance, -100)
