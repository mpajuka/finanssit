from tkinter import ttk, constants
from financeservice import FinanceService


class Account:
    def __init__(self, root, handle_login, handle_profile, user):
        self._root = root
        self._handle_login = handle_login
        self._handle_profile = handle_profile
        self._frame = None
        self._app = FinanceService()
        self._profile_tree = None
        self._profile = None
        self._user = user
        self._new_profile_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def on_click(self, event):
        item = self._profile_tree.selection()[0]
        if item:
            profile_name = self._profile_tree.item(item, "values")[0]
            get_profile = self._app.find_profile(profile_name)
            if get_profile:
                self._profile = get_profile
                self._handle_profile(self._profile)

    def create_profile(self):
        profile_name = self._new_profile_entry.get()
        if profile_name != "":
            self._profile = self._app.create_profile(profile_name, self._user.username)
            if self._profile:
                self._profile_tree.insert("", "end", values=self._profile.name)
        self._new_profile_entry.delete(0, "end")




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
        profiles_separator = ttk.Separator(
            master=self._frame, orient="horizontal")
        profiles_label = ttk.Label(master=self._frame, text="List of profiles",
                                   font=("Arial", 16))

        self._profile_tree = ttk.Treeview(master=self._frame, columns=col,
                                          show='headings')

        self._new_profile_entry = ttk.Entry(master=self._frame)

        create_profile_button = ttk.Button(
            master=self._frame,
            text="Create profile",
            command=self.create_profile
        )
        self._profile_tree.heading(col, text=col)

        label.grid(row=0, column=0, padx=5, pady=5)
        button.grid(row=0, column=1, padx=5, pady=5)
        profiles_separator.grid(row=1, columnspan=2, sticky="ew", pady=10)
        profiles_label.grid(row=2, column=0, columnspan=2)
        self._profile_tree.grid(row=3, column=0, columnspan=2)
        self._new_profile_entry.grid(row=4, column=0)
        create_profile_button.grid(row=4, column=1)

        db_profiles = self._app.return_profiles(self._user.username)
        for profile in db_profiles:
            self._profile_tree.insert("", "end", values=profile.name)

        self._profile_tree.bind("<Double-1>", self.on_click)
