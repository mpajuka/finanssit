from tkinter import ttk, constants
import tkinter as tk
from financeservice import FinanceService
from compound_interest_calc import calculate_investments
from transactionrepository import Transaction

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

    def add_or_edit_transaction(self, transaction_name, transaction_amount, notification, radio_value, transaction_id=None):
        name = transaction_name.get()
        amount_entry = transaction_amount.get()
        if transaction_id:
            edit_transaction = self._app.edit_transaction(name, amount_entry, self._profile, radio_value, transaction_id)
            if isinstance(edit_transaction, Transaction):
                notification.config(text="Transaction updated!")
                self._transaction_name_entry.delete(0, "end")
                self._transaction_amount_entry.delete(0, "end")
                self._transaction_tree.delete(*self._transaction_tree.get_children())
                self.refresh_transactions()
                
                self._total_balance.config(text=f"Current Balance: {self.get_balance()} €")
            else:
                notification.config(text=edit_transaction)


        else:
            new_transaction = self._app.create_transaction(name, amount_entry, self._profile, radio_value)
            if isinstance(new_transaction, Transaction):
                notification.config(text="New transaction added!")
                self._transaction_name_entry.delete(0, "end")
                self._transaction_amount_entry.delete(0, "end")
                self._transaction_tree.delete(*self._transaction_tree.get_children())
                self.refresh_transactions()
                self._total_balance.config(text=f"Current Balance: {self.get_balance()} €")
            else:
                notification.config(text=new_transaction)


    def open_transaction_window(self, transaction_id=None):
        transaction_window = tk.Toplevel(self._frame)
        transaction_window.wm_transient(self._frame)
        transaction_window.grab_set()

        transaction_window.geometry(
            f"+{self._root.winfo_x() + 50}+{self._root.winfo_y() + 50}"
        )
        transaction_name_label = ttk.Label(
            master=transaction_window, text="Transaction name")
        self._transaction_name_entry = ttk.Entry(master=transaction_window)
        transaction_amount_label = ttk.Label(
            master=transaction_window, text="Amount (€)")
        self._transaction_amount_entry = ttk.Entry(master=transaction_window)
        notification = ttk.Label(master=transaction_window, text="")

        v = tk.StringVar()
        v.set(value="")


        income = ttk.Radiobutton(master=transaction_window,
                                 text="Income",
                                 value="Income",
                                 variable=v)
        
        expense = ttk.Radiobutton(master=transaction_window,
                                  text="Expense",
                                  value="Expense",
                                  variable=v)
        
        if transaction_id:
            edit_transaction_button = ttk.Button(master=transaction_window, text="Edit transaction",
                                                command=lambda: self.add_or_edit_transaction(
                                                    self._transaction_name_entry,
                                                    self._transaction_amount_entry,
                                                    notification,
                                                    v.get(),
                                                    transaction_id))
            edit_transaction_button.grid(row=4, columnspan=2)

        else:
            add_transaction_button = ttk.Button(master=transaction_window, text="Add transaction",
                                                command=lambda: self.add_or_edit_transaction(
                                                    self._transaction_name_entry,
                                                    self._transaction_amount_entry,
                                                    notification,
                                                    v.get()))
            add_transaction_button.grid(row=4, columnspan=2)

        transaction_name_label.grid(row=0, column=0)
        self._transaction_name_entry.grid(row=0, column=1)
        transaction_amount_label.grid(row=1, column=0)
        self._transaction_amount_entry.grid(row=1, column=1)
        notification.grid(row=2, columnspan=2)
        income.grid(row=3, column=0)
        expense.grid(row=3, column=1)


    def on_click(self, event):
        item = self._transaction_tree.selection()[0]
        if item:
            transaction_id = self._transaction_tree.item(item, "values")[0]
            self.open_transaction_window(transaction_id)
        return event

    def open_compound_interest_calculator(self):
        cic_window = tk.Toplevel(self._frame)
        cic_window.wm_transient(self._frame)
        cic_window.grab_set()

        cic_window.geometry(
            f"+{self._root.winfo_x() + 50}+{self._root.winfo_y() + 50}"
        )

        ttk.Label(master=cic_window, text="Compound Interest Calculator",
                  font=("TkDefaultFont", 20)).grid(row=0, column=0, columnspan=2)

        cic_curr_value_ent = ttk.Entry(master=cic_window)
        cic_curr_value_ent.grid(row=1, column=1)
        ttk.Label(master=cic_window, text="Current value of investments (€)").grid(
            row=1, column=0)

        cic_monthly_ctrb_ent = ttk.Entry(master=cic_window)
        cic_monthly_ctrb_ent.grid(row=2, column=1)
        ttk.Label(master=cic_window, text="Monthly contribution (€)").grid(
            row=2, column=0)

        cic_est_return_ent = ttk.Entry(master=cic_window)
        cic_est_return_ent.grid(row=3, column=1)
        ttk.Label(master=cic_window, text="Anticipated return for investment (%)").grid(
            row=3, column=0)

        cic_time_hrz_ent = ttk.Entry(master=cic_window)
        cic_time_hrz_ent.grid(row=4, column=1)
        ttk.Label(
            master=cic_window, text="Investment time horizon (years)").grid(row=4, column=0)

        ttk.Button(master=cic_window,
                   text="Calculate",
                   command=lambda:
                       calculate_investments(
                           cic_curr_value_ent.get(),
                           cic_monthly_ctrb_ent.get(),
                           cic_est_return_ent.get(),
                           cic_time_hrz_ent.get())).grid(row=5, column=0, columnspan=2)

    def get_balance(self):
        return f"{self._app.return_profile_balance(self._profile):.2f}"
    
    def refresh_transactions(self):
        transactions = self._app.return_transactions(self._profile)
        transactions.reverse()
        for transaction in transactions:
            self._transaction_tree.insert("", "end", values=(transaction.id,
                                                             transaction.name,
                                                             f"{transaction.amount:.2f}"))

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

        investment_calculator_btn = ttk.Button(
            master=self._frame,
            text="Compound Interest Calculator",
            command=self.open_compound_interest_calculator
        )

        self._total_balance = ttk.Label(master=self._frame, 
                                        text=f"Current Balance: {self.get_balance()} €",
                                        font=("TkDefaultFont", 16))

        transaction_scroll = ttk.Scrollbar(self._frame, orient="vertical")

        self._transaction_tree = ttk.Treeview(master=self._frame, columns=('ID', 'Name', 'Amount'),
                                          show='headings')

        transaction_scroll.config(command=self._transaction_tree.yview)
        self._transaction_tree.configure(yscrollcommand=transaction_scroll.set)
        self._transaction_tree.heading("ID", text="ID")
        self._transaction_tree.heading("Name", text="Name")
        self._transaction_tree.heading("Amount", text="Amount (€)")

        label.grid(row=0, column=0, columnspan=2)
        button.grid(row=1, column=0, columnspan=2)
        add_transaction_button.grid(row=2, column=0, columnspan=2)
        investment_calculator_btn.grid(row=3, column=0, columnspan=2)
        self._total_balance.grid(row=4, column=0, columnspan=2)
        self._transaction_tree.grid(row=5, column=0)
        transaction_scroll.grid(row=5, column=1, sticky="ns")

        self.refresh_transactions()

        self._transaction_tree.bind("<Double-1>", self.on_click)
