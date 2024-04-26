from tkinter import ttk, constants
import tkinter as tk
from financeservice import FinanceService
from compound_interest_calc import calculate_investments
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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

    def open_compound_interest_calculator(self):
        cic_window = tk.Toplevel(self._frame)
        cic_window.wm_transient(self._frame)
        cic_window.grab_set()

        x = self._root.winfo_x() + 50
        y = self._root.winfo_y() + 50
        cic_window.geometry("+{}+{}".format(x, y))

        cic_title = ttk.Label(master=cic_window, text="Compound Interest Calculator",
                              font=("TkDefaultFont", 20))
        cic_curr_value_ent = ttk.Entry(master=cic_window)
        cic_curr_value_txt = ttk.Label(
            master=cic_window, text="Current value of investments (€)")

        cic_monthly_ctrb_ent = ttk.Entry(master=cic_window)
        cic_monthly_ctrb_txt = ttk.Label(
            master=cic_window, text="Monthly contribution (€)")

        cic_est_return_ent = ttk.Entry(master=cic_window)
        cic_est_return_txt = ttk.Label(
            master=cic_window, text="Anticipated return for investment (%)")

        cic_time_hrz_ent = ttk.Entry(master=cic_window)
        cic_time_hrz_txt = ttk.Label(
            master=cic_window, text="Investment time horizon (years)")

        cic_calculate_btn = ttk.Button(master=cic_window, text="Calculate",
                                       command=lambda: self.calculate_cic(
                                           cic_curr_value_ent,
                                           cic_monthly_ctrb_ent,
                                           cic_est_return_ent,
                                           cic_time_hrz_ent))

        cic_title.grid(row=0, column=0, columnspan=2)
        cic_curr_value_txt.grid(row=1, column=0)
        cic_curr_value_ent.grid(row=1, column=1)

        cic_monthly_ctrb_txt.grid(row=2, column=0)
        cic_monthly_ctrb_ent.grid(row=2, column=1)

        cic_est_return_txt.grid(row=3, column=0)
        cic_est_return_ent.grid(row=3, column=1)

        cic_time_hrz_txt.grid(row=4, column=0)
        cic_time_hrz_ent.grid(row=4, column=1)

        cic_calculate_btn.grid(row=5, column=0, columnspan=2)

    def calculate_cic(self, curr_value, contribution, est_return, time):
        cic_window = tk.Toplevel(self._frame)
        cic_window.wm_transient(self._frame)
        cic_window.grab_set()

        fig, ax = calculate_investments(curr_value, contribution,
                                        est_return,
                                        time)

        canvas = FigureCanvasTkAgg(fig, master=cic_window)

        canvas.get_tk_widget().pack()

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

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        add_transaction_button.grid(row=2, column=0)
        investment_calculator_btn.grid(row=3, column=0)
