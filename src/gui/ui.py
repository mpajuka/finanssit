from gui.register import Register
from gui.login import Login
from gui.account import Account
from gui.profile import Profile


class UI:
    """Main UI component for handling the view switching and window initialization
    """

    def __init__(self, root):
        """initializes the main UI component handler

        Args:
            root (Tk): tkinter root view component
        """
        self._root = root
        self._username = None
        self._password = None
        self._notification = None
        self._current_view = None

    def start(self):
        """starts the UI session with the login component
        """
        self._show_login()

    def _hide_current_view(self):
        """destroys the currently visible view component
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_login_view(self):
        """Transfer the view to the login component from the previous
        """
        self._show_login()

    def _handle_register_view(self):
        """Transfer the view to the register component from the previous
        """
        self._show_register()

    def _handle_account_view(self, user):
        """Transfer the view to the account selection component from the previous

        Args:
            user (User): the user of the existing session
        """
        self._show_account(user)

    def _handle_profile_view(self, profile):
        """Transfer the view to the profile view component from the previous

        Args:
            profile (Profile): the user selected profile 
        """
        self._show_profile(profile)

    def _show_profile(self, profile):
        """initialize the profile component view

        Args:
            profile (Profile): selected profile
        """
        self._hide_current_view()

        self._current_view = Profile(
            self._root, self._handle_login_view, profile)

        self._current_view.pack()

    def _show_register(self):
        """initialize the register component view
        """
        self._hide_current_view()

        self._current_view = Register(self._root, self._handle_login_view)

        self._current_view.pack()

    def _show_login(self):
        """initialize the login component view
        """
        self._hide_current_view()

        self._current_view = Login(self._root, self._handle_register_view,
                                   self._handle_account_view)

        self._current_view.pack()

    def _show_account(self, user):
        """initialize the account selection component view

        Args:
            user (User): session user
        """
        self._hide_current_view()

        self._current_view = Account(self._root, self._handle_login_view,
                                     self._handle_profile_view, user)

        self._current_view.pack()
