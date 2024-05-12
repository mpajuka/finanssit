from tkinter import ttk, constants
from financeservice import FinanceService
from repositories.userrepository import User


class Register:
    """UI component for the registration view
    """

    def __init__(self, root, handle_login) -> None:
        """initializes the variables for the register view component

        Args:
            root (Tk): tkinter root component
            handle_login (any): handles the initialization of the login view
        """
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._app = FinanceService()
        self._initialize()

    def pack(self):
        """packs the tkinter view component
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """destroys the tkinter frame
        """
        self._frame.destroy()

    def _initialize(self):
        """initializes the tkinter components of the view
        """
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
                                     command=lambda:
                                         self.handle_register(
                                             self._username.get().strip(), self._password.get()))

        login_button = ttk.Button(
            master=self._frame,
            text="Return to login",
            command=self._handle_login
        )

        heading_label.grid(row=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username.grid(row=1, column=1,
                            sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password.grid(row=2, column=1,
                            sticky=(constants.E, constants.W), padx=5, pady=5)
        self._notification.grid(columnspan=2, rowspan=2,
                                sticky=(constants.E, constants.W),
                                padx=5, pady=5)
        register_button.grid(columnspan=2,
                             sticky=(constants.E, constants.W),
                             padx=5, pady=5)
        login_button.grid(columnspan=2,
                          sticky=(constants.E, constants.W),
                          padx=5, pady=5)

    def handle_register(self, username, password):
        """handles the registering event of a new user

        Args:
            username (str): new username
            password (str): new user password
        """
        new_user = self._app.register(username, password)
        if isinstance(new_user, User):
            self._username.delete(0, "end")
            self._password.delete(0, "end")
            self._notification.config(text="New user created!")
        else:
            self._notification.config(text=new_user)
