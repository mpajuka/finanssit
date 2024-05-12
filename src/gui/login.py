from tkinter import ttk, constants
from financeservice import FinanceService


class Login:
    """UI component for the login view of the application
    """

    def __init__(self, root, handle_register, handle_account) -> None:
        """Initializes the variables for the login view component

        Args:
            root (Tk): tkinter root window
            handle_register (any): handles the initialization of the registering view
            handle_account (any): handles the initialization of the account selection view
        """
        self._root = root
        self._frame = None
        self._app = FinanceService()
        self._handle_register = handle_register
        self._handle_account = handle_account
        self._initialize()

    def pack(self):
        """packs the tkinter view component
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """destroy the tkinter frame
        """
        self._frame.destroy()

    def _initialize(self):
        """initializes the tkinter components of the view
        """
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Finanssit | Login", font=("TkDefaultFont", 20))

        login_username_label = ttk.Label(master=self._frame, text="Username")
        self._login_username = ttk.Entry(master=self._frame)

        login_password_label = ttk.Label(master=self._frame, text="Password")
        self._login_password = ttk.Entry(master=self._frame, show="*")

        self._notification = ttk.Label(master=self._frame, text="")

        login_button = ttk.Button(
            master=self._frame, text="Log in", command=self._handle_login)
        self._frame.bind("<Return>", self._handle_login)

        register_button = ttk.Button(
            master=self._frame,
            text="Register view",
            command=self._handle_register
        )

        heading_label.grid(row=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        login_username_label.grid(row=1, column=0, padx=5, pady=5)
        self._login_username.grid(
            row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        login_password_label.grid(row=2, column=0, padx=5, pady=5)
        self._login_password.grid(
            row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._notification.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _handle_login(self):
        """handles the logging in event of the user
        """
        username = self._login_username.get()
        password = self._login_password.get()
        user = self._app.login(username, password)
        if user is None:
            self._notification.config(text="user not found")
            self._notification.after(
                5000, lambda: self._notification.config(text=""))
        else:
            self._handle_account(user)
