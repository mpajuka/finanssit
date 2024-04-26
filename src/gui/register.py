from tkinter import ttk, constants
from financeservice import FinanceService


class Register:
    def __init__(self, root, handle_login) -> None:
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._app = FinanceService()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame,
                                  text="Finanssit | Create an account", font=("TkDefaultFont", 20))

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password = ttk.Entry(master=self._frame, show="*")

        self._notification = ttk.Label(master=self._frame, text="")

        register_button = ttk.Button(master=self._frame,
                                     text="Create account",
                                     command=self._handle_register)

        login_button = ttk.Button(
            master=self._frame,
            text="Return to login",
            command=self._handle_login
        )

        heading_label.grid(row=0, columnspan=2, sticky=constants.W)
        username_label.grid(row=1, column=0)
        self._username.grid(row=1, column=1,
                            sticky=(constants.E, constants.W))

        password_label.grid(row=2, column=0)
        self._password.grid(row=2, column=1,
                            sticky=(constants.E, constants.W))
        self._notification.grid(columnspan=2, rowspan=2,
                                sticky=(constants.E, constants.W),
                                padx=5, pady=5)
        register_button.grid(columnspan=2,
                             sticky=(constants.E, constants.W),
                             padx=5, pady=5)
        login_button.grid(columnspan=2,
                          sticky=(constants.E, constants.W),
                          padx=5, pady=5)

    def _handle_register(self):
        username = self._username.get().strip()
        password = self._password.get()
        if username == "":
            self._notification.config(
                text="Error: username must not be empty")
            return False
        if len(password) < 8:
            self._notification.config(
                text="Error: password must contain at least\n" +
                "8 characters, 1 number and\n" +
                "1 special character")
            return False
        if not any(c.isnumeric() for c in password):
            self._notification.config(
                text="Error: password must contain at least\n" +
                "1 number and 1 special character")
            return False
        if password.isalnum():
            self._notification.config(
                text="Error: password must contain at least\n" +
                "1 special character")
            return False
        new_user = self._app.register(username, password)
        if new_user is False:
            self._notification.config(text="Error: username not available.")
        if new_user:
            self._username.delete(0, "end")
            self._password.delete(0, "end")
            self._notification.config(text="New user created!")
            return True
        return False
