from gui.register import Register
from gui.login import Login
from gui.account import Account
from gui.profile import Profile


class UI:
    def __init__(self, root):
        self._root = root
        self._username = None
        self._password = None
        self._notification = None
        self._current_view = None

    def start(self):
        self._show_login()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_login_view(self):
        self._show_login()

    def _handle_register_view(self):
        self._show_register()

    def _handle_account_view(self, user):
        self._show_account(user)

    def _handle_profile_view(self, profile):
        self._show_profile(profile)

    def _show_profile(self, profile):
        self._hide_current_view()

        self._current_view = Profile(
            self._root, self._handle_login_view, profile)

        self._current_view.pack()

    def _show_register(self):
        self._hide_current_view()

        self._current_view = Register(self._root, self._handle_login_view)

        self._current_view.pack()

    def _show_login(self):
        self._hide_current_view()

        self._current_view = Login(self._root, self._handle_register_view,
                                   self._handle_account_view)

        self._current_view.pack()

    def _show_account(self, user):
        self._hide_current_view()

        self._current_view = Account(self._root, self._handle_login_view,
                                     self._handle_profile_view, user)

        self._current_view.pack()
