from tkinter import ttk, constants, Scale
import tkinter as tk
from tkcalendar import DateEntry
from financeservice import FinanceService
from compound_interest_calc import format_input
from repositories.transactionrepository import Transaction


class Profile:
    """UI component for the individual profile view
    """

    def __init__(self, root, handle_login, profile):
        """initializes the UI component variables for the profile

        Args:
            root (Tk): the root component for the view
            handle_login (any): handles the initialization of the login view
            profile (Profile): the opened profile in the session
        """
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._app = FinanceService()
        self._profile_tree = None
        self._profile = profile
        self._transaction_amount_entry = None
        self._transaction_name_entry = None
        self._initialize()
        self._date = None

    def pack(self):
        """packs the tkinter view component
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """destroy the profile view 
        """
        self._frame.destroy()

    def add_or_edit_transaction(self, transaction_name, transaction_amount, notification,
                                radio_value,
                                date,
                                transaction_id=None):
        """handles the event of adding a transaction event, or editing an existing one

        Args:
            transaction_name (ttk.Entry): name of the transaction
            transaction_amount (ttk.Entry): amount of the transaction
            notification (ttk.Label): notification label to display a possible error message
            radio_value (ttk.RadioButton): 
                the radio button value whether the transaction is an expense or income
            date (DateEntry): the tkinter component value for the date of the transaction
            transaction_id (int, optional): 
                the transaction id of an existing transaction
                handles the editing if one exists, otherwise a new transaction. 
                Defaults to None.
        """
        name = transaction_name.get()
        amount_entry = transaction_amount.get()
        formatted_amount_entry = amount_entry.replace(
            ",", ".").replace(" ", "")
        if transaction_id:
            edit_transaction = self._app.edit_transaction(
                name, formatted_amount_entry, self._profile, radio_value, transaction_id, date)
            if isinstance(edit_transaction, Transaction):
                notification.config(text="Transaction updated!")
                self._transaction_name_entry.delete(0, "end")
                self._transaction_amount_entry.delete(0, "end")
                self._transaction_tree.delete(
                    *self._transaction_tree.get_children())
                self.refresh_transactions()
                self.refresh_total_balance()

            else:
                notification.config(text=edit_transaction)
        else:
            self.add_transaction(name, formatted_amount_entry, notification, radio_value, date)


    def add_transaction(self, name, formatted_amount_entry, notification, radio_value,
                        date):
        """add the transaction based on the input information

        Args:
            name (str): transactions name
            formatted_amount_entry (str): formatted transaction amount
            notification (ttk.Label): error notification label
            radio_value (str): transaction type value
            date (str): date of transaction
        """
        new_transaction = self._app.create_transaction(
            name, formatted_amount_entry, self._profile, radio_value, date)
        if isinstance(new_transaction, Transaction):
            notification.config(text="New transaction added!")
            self._transaction_name_entry.delete(0, "end")
            self._transaction_amount_entry.delete(0, "end")
            self._transaction_tree.delete(
                *self._transaction_tree.get_children())
            self.refresh_transactions()
            self.refresh_total_balance()
        else:
            notification.config(text=new_transaction)

    def remove_transaction_window(self, transaction_window, transaction_id):
        """transaction removal window with confirmal prompt

        Args:
            transaction_window (tk.Toplevel): root window
            transaction_id (int): the transactions identifier
        """
        confirmation_window = tk.Toplevel(transaction_window)
        confirmation_window.wm_transient(transaction_window)
        confirmation_window.grab_set()

        # center the window
        confirmation_window.geometry(
            f"+{self._root.winfo_x() + 50}+{self._root.winfo_y() + 50}"
        )

        confirmation_label = ttk.Label(master=confirmation_window,
                                       text="Are you sure you want to delete this transaction?")
        confirmation_yes_btn = ttk.Button(master=confirmation_window,
                                          text="Yes",
                                          command=lambda: self.handle_remove_transaction(
                                              transaction_id,
                                              transaction_window))
        confirmation_no_btn = ttk.Button(master=confirmation_window,
                                         text="No",
                                         command=confirmation_window.destroy)

        confirmation_label.grid(row=0, columnspan=2)
        confirmation_yes_btn.grid(row=1, columnspan=2)
        confirmation_no_btn.grid(row=2, columnspan=3)

    def handle_remove_transaction(self, transaction_id, transaction_window):
        """handles the confirmed removal event of a transaction

        Args:
            transaction_id (int): 
                the identifier of the transaction to be deleted
            transaction_window (tk.Toplevel): the root tkinter window
        """
        result = self._app.remove_transaction(transaction_id)
        if result:
            self._transaction_tree.delete(
                *self._transaction_tree.get_children())
            self.refresh_transactions()
            self.refresh_total_balance()
            transaction_window.destroy()

    def select_transaction_window(self, transaction_id):
        """handles opening window after a user click of the
        treeview component row

        Args:
            transaction_id (int): clicked transactions identifier
        """
        select_transaction_window = tk.Toplevel(self._frame)
        select_transaction_window.wm_transient(self._frame)
        select_transaction_window.geometry(
            f"+{self._root.winfo_x() + 50}+{self._root.winfo_y() + 50}"
        )
        select_transaction_window.wait_visibility()
        select_transaction_window.grab_set()

        transaction = self._app.get_transaction(transaction_id)

        transaction_data = ttk.Label(master=select_transaction_window,
                                     text=f"Name: {transaction.name}\nAmount: " +
                                     f"{transaction.amount} €\nDate: {transaction.date}",
                                     font=("TkDefaultFont", 16))

        edit_transaction_button = ttk.Button(master=select_transaction_window,
                                             text="Edit transaction",
                                             command=lambda:
                                             self.open_transaction_window(transaction_id))

        remove_transaction_button = ttk.Button(master=select_transaction_window,
                                               text="Remove transaction",
                                               command=lambda: self.remove_transaction_window(
                                                   select_transaction_window, transaction_id))
        transaction_data.grid(row=0, columnspan=2, padx=10, pady=10)
        edit_transaction_button.grid(row=1, columnspan=2, padx=10, pady=5)
        remove_transaction_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def open_transaction_window(self, transaction_id=None):
        """handles the opening of a new transaction window

        Args:
            transaction_id (int, optional): 
                the identifier of a possibly existing transaction, 
                triggers the editing view instead of creation, 
                otherwise addition. Defaults to None.
        """
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

        self._date = DateEntry(master=transaction_window,
                               date_pattern="yyyy-mm-dd")
        date_label = ttk.Label(master=transaction_window, text="Date")

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
            title = ttk.Label(master=transaction_window, text="Edit transaction",
                              font=("TkDefaultFont", 18))
            edit_transaction_button = ttk.Button(master=transaction_window, text="Confirm edit",
                                                 command=lambda: self.add_or_edit_transaction(
                                                     self._transaction_name_entry,
                                                     self._transaction_amount_entry,
                                                     notification,
                                                     v.get(),
                                                     self._date.get_date(),
                                                     transaction_id))
            edit_transaction_button.grid(row=6, columnspan=2)

        else:
            title = ttk.Label(master=transaction_window, text="Add transaction",
                              font=("TkDefaultFont", 18))

            add_transaction_button = ttk.Button(master=transaction_window, text="Confirm add",
                                                command=lambda: self.add_or_edit_transaction(
                                                    self._transaction_name_entry,
                                                    self._transaction_amount_entry,
                                                    notification,
                                                    v.get(),
                                                    self._date.get_date()))
            add_transaction_button.grid(row=6, columnspan=2)

        title.grid(row=0, columnspan=2)
        transaction_name_label.grid(row=1, column=0)
        self._transaction_name_entry.grid(row=1, column=1)
        transaction_amount_label.grid(row=2, column=0)
        self._transaction_amount_entry.grid(row=2, column=1)
        date_label.grid(row=3, column=0)
        self._date.grid(row=3, column=1)
        notification.grid(row=4, columnspan=2)
        income.grid(row=5, column=0)
        expense.grid(row=5, column=1)

    def on_click(self, event):
        """handles the on click event of the transaction treeview component

        Args:
            event (any): transaction click event

        Returns:
            event (any): transaction click event
        """
        item = self._transaction_tree.selection()[0]
        if item:
            transaction_id = self._transaction_tree.item(item, "values")[0]
            self.select_transaction_window(transaction_id)
        return event

    def open_compound_interest_calculator(self):
        """handles the opening of the compound interest calculator view
        """
        cic_window = tk.Toplevel(self._frame)
        cic_window.wm_transient(self._frame)
        cic_window.grab_set()

        cic_window.geometry(
            f"+{self._root.winfo_x() + 50}+{self._root.winfo_y() + 50}"
        )

        ttk.Label(master=cic_window, text="Compound Interest Calculator",
                  font=("TkDefaultFont", 20)).grid(row=0, column=0, columnspan=2)

        cic_curr_value_ent = Scale(master=cic_window, from_=0, to=50000, orient="horizontal",
                                   tickinterval=5000, length=600)
        cic_curr_value_ent.grid(row=1, column=1, padx=5)
        ttk.Label(master=cic_window, text="Initial lump sum investment (€)").grid(
            row=1, column=0)

        cic_monthly_ctrb_ent = Scale(master=cic_window, from_=0, to=5000, orient="horizontal",
                                     tickinterval=500, length=600)
        cic_monthly_ctrb_ent.grid(row=2, column=1, padx=5)
        ttk.Label(master=cic_window, text="Monthly contribution (€)").grid(
            row=2, column=0)

        cic_est_return_ent = Scale(master=cic_window, from_=0, to=20, orient="horizontal",
                                   tickinterval=1, length=600)
        cic_est_return_ent.grid(row=3, column=1)
        ttk.Label(master=cic_window, text="Anticipated return for investment (%)").grid(
            row=3, column=0)

        cic_time_hrz_ent = Scale(master=cic_window, from_=0, to=60, orient="horizontal",
                                 tickinterval=5, length=600)
        cic_time_hrz_ent.grid(row=4, column=1)
        ttk.Label(
            master=cic_window, text="Investment time horizon (years)").grid(row=4, column=0)

        ttk.Button(master=cic_window,
                   text="Calculate",
                   command=lambda:
                        format_input(
                            cic_curr_value_ent.get(),
                            cic_monthly_ctrb_ent.get(),
                            cic_est_return_ent.get(),
                            cic_time_hrz_ent.get())).grid(row=6, column=0, columnspan=2)

    def get_balance(self):
        """handles the refreshing of the account balance

        Returns:
            float: floating point value if any transactions exist, otherwise 0.00
        """
        if self._app.return_profile_balance(self._profile):
            return f"{self._app.return_profile_balance(self._profile):.2f}"
        return 0.00

    def refresh_total_balance(self):
        """refreshes the existing total balance when a new transaction event occurs
        """
        self._total_balance.config(
            text=f"Current Balance: {self.get_balance()} €")

    def refresh_transactions(self):
        """re-initializes the treeviews components
        """
        transactions = self._app.return_transactions(self._profile)
        transactions.reverse()
        for transaction in transactions:
            self._transaction_tree.insert("", "end", values=(transaction.id,
                                                             transaction.name,
                                                             f"{transaction.amount:.2f}",
                                                             transaction.date))
    # generoitu koodi alkaa

    def sort_column(self, transaction_tree, col, reverse):
        """sorts the treeview table based on the click event of each column heading

        Args:
            transaction_tree (ttk.TreeView): the treeview component of the windows
            col (str): treeview column
            reverse (bool): argument for the order of the column
        """
        data = [(transaction_tree.set(child, col), child)
                for child in transaction_tree.get_children('')]
        data.sort(reverse=reverse)
        for index, (_, child) in enumerate(data):
            transaction_tree.move(child, '', index)
            transaction_tree.heading(col, command=lambda:
                                     self.sort_column(transaction_tree, col, not reverse))
    # generoitu koodi päättyy

    def _initialize(self):
        """initializes the tkinter components of the view
        """
        self._frame = ttk.Frame(master=self._root)
        profile_name = ttk.Label(master=self._frame, text=self._profile.name,
                                 font=("TkDefaultFont", 20))

        logout_button = ttk.Button(
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

        self._transaction_tree = ttk.Treeview(master=self._frame,
                                              columns=("ID", "Name",
                                                       "Amount", "Date"),
                                              show='headings', height=20)

        transaction_scroll.config(command=self._transaction_tree.yview)
        self._transaction_tree.configure(yscrollcommand=transaction_scroll.set)

        self._transaction_tree.heading("ID", text="ID")
        # komennon .heading(command=)-osa generoitua
        self._transaction_tree.heading("Name", text="Name", command=lambda: self.sort_column(
            self._transaction_tree, "Name", False))
        self._transaction_tree.heading("Amount", text="Amount (€)",
                                       command=lambda: self.sort_column(
                                           self._transaction_tree, "Amount", False))
        self._transaction_tree.heading("Date", text="Date", command=lambda: self.sort_column(
            self._transaction_tree, "Date", False))
        # osittain generoitu osa päättyy

        self._transaction_tree.column("ID", width=50)

        profile_name.grid(row=0, column=0, padx=5, pady=5)
        logout_button.grid(row=0, column=1, padx=5, pady=5)
        self._total_balance.grid(row=1, column=0, rowspan=2, padx=5, pady=5)

        add_transaction_button.grid(row=1, column=1, padx=5, pady=5)

        investment_calculator_btn.grid(row=2, column=1, padx=5, pady=5)

        self._transaction_tree.grid(
            row=5, column=0, columnspan=2, padx=5, pady=5)
        transaction_scroll.grid(row=5, column=2, sticky="ns", padx=5, pady=5)

        self.refresh_transactions()

        self._transaction_tree.bind("<Double-1>", self.on_click)
