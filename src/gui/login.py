from tkinter import ttk, constants
from financeservice import FinanceService

class Login:
    def __init__(self, root, handle_register, handle_account) -> None:
        self._root = root
        self._handle_register = handle_register
        self._handle_account = handle_account
        self._frame = None
        self._app = FinanceService()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)


        heading_label = ttk.Label(master=self._frame, text="Finanssit | Login")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password = ttk.Entry(master=self._frame)

        self._notification = ttk.Label(master=self._frame, text="")

        login_button = ttk.Button(master=self._frame, text="Log in", command=self._handle_login)

        register_button = ttk.Button(
            master=self._frame,
            text="Register view",
            command=self._handle_register
        )

        heading_label.grid(row=0, columnspan=2, sticky=constants.W)
        username_label.grid(row=1, column=0)
        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W))

        password_label.grid(row=2, column=0)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W))
        self._notification.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _handle_login(self):
        username = self._username.get()
        password = self._password.get()
        user = self._app.login(username, password)
        if user is None:
            self._notification.config(text="user not found")
            self._notification.after(5000, lambda: self._notification.config(text=""))
            return False
        self._handle_account()
        return True
