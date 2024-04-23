from tkinter import ttk, constants
from financeservice import FinanceService


class Profile:
    def __init__(self, root, handle_login, profile):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._app = FinanceService()
        self._profile_tree = None
        self._profile = profile
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
        
    def add_transaction(self):
        pass

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=self._profile.name,
                          font=("TkDefaultFont", 20))

        button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._handle_login
        )
        
        add_transaction_button = ttk.Button(
            master=self._frame,
            text="Add transaction",
            command=self.add_transaction
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        add_transaction_button.grid(row=2, column=0)
