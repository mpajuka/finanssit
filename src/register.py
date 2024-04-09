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
                
        heading_label = ttk.Label(master=self._frame, text="Finanssit | Create an account")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password = ttk.Entry(master=self._frame)
        
        self._notification = ttk.Label(master=self._frame, text="")
        
        register_button = ttk.Button(master=self._frame, text="Create account", command=self._handle_register)

        login_button = ttk.Button(
            master=self._frame,
            text="Return to login",
            command=self._handle_login
        )

        heading_label.grid(row=0, columnspan=2, sticky=constants.W)
        username_label.grid(row=1, column=0)
        self._username.grid(row=1, column=1, sticky=(constants.E, constants.W))

        password_label.grid(row=2, column=0)
        self._password.grid(row=2, column=1, sticky=(constants.E, constants.W))
        self._notification.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
    
    def _handle_register(self):
        username = self._username.get()
        password = self._password.get()
        newUser = self._app.register(username, password)
        if newUser: 
            self._username.delete(0, "end")
            self._password.delete(0, "end")
            self._notification.config(text="New user created!")