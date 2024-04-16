from tkinter import ttk, constants
from financeservice import FinanceService

class Account:
    def __init__(self, root, handle_login, user):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._app = FinanceService()
        self._profile_tree = None
        self._user = user
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
   
    def on_click(self, event):
        item = self._profile_tree.selection()[0]
        print(self._profile_tree.item(item, "values")[0])


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Welcome to Finanssit!",
                          font=("TkDefaultFont", 20))

        button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._handle_login
        )
        col = 'Name'
        profiles_separator = ttk.Separator(master=self._frame, orient="horizontal")
        profiles_label = ttk.Label(master=self._frame, text="List of profiles",
                                   font=("Arial",16))

        self._profile_tree = ttk.Treeview(master=self._frame, columns=col,
                                     show='headings')

        self._profile_tree.heading(col, text=col)


        label.grid(row=0, column=0, padx=5, pady=5)
        button.grid(row=0, column=1, padx=5, pady=5)
        profiles_separator.grid(row=1, columnspan=2, sticky="ew", pady=10)
        profiles_label.grid(row=2, column=0, columnspan=2)
        self._profile_tree.grid(row=3, column=0, columnspan=2)

        db_profiles = self._app.return_profiles(self._user.username)
        for profile in db_profiles:
            self._profile_tree.insert("", "end", values=profile.name)

        self._profile_tree.bind("<Double-1>", self.on_click)
