import unittest
from financeservice import FinanceService
from userrepository import User

class TestFinanceService(unittest.TestCase):
    def setUp(self):
        self._app = FinanceService()
        self._user = None

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
