from tkinter import ttk, constants
import tkinter as tk
from financeservice import FinanceService


class Profile:
    def __init__(self, root, handle_login, profile):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._app = FinanceService()
        self._profile_tree = None
        self._profile = profile
        self._transaction_amount_entry = None
        self._transaction_name_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def add_transaction(self):
        name = self._transaction_name_entry.get()
        amount = self._transaction_amount_entry.get()
        print(name, amount)

    def open_transaction_window(self):
        transaction_window = tk.Toplevel(self._frame)
        transaction_window.wm_transient(self._frame)
        transaction_window.grab_set()
        transaction_name_label = ttk.Label(
            master=transaction_window, text="Transaction name")
        self._transaction_name_entry = ttk.Entry(master=transaction_window)
        transaction_amount_label = ttk.Label(
            master=transaction_window, text="Amount")
        self._transaction_amount_entry = ttk.Entry(master=transaction_window)
        add_transaction_button = ttk.Button(master=transaction_window, text="Add transaction",
                                            command=self.add_transaction)
        transaction_name_label.grid(row=0, column=0)
        self._transaction_name_entry.grid(row=0, column=1)
        transaction_amount_label.grid(row=1, column=0)
        self._transaction_amount_entry.grid(row=1, column=1)
        add_transaction_button.grid(row=2, columnspan=2)

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
            command=self.open_transaction_window
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        add_transaction_button.grid(row=2, column=0)
