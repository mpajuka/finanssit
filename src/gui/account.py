from tkinter import ttk, constants
from financeservice import FinanceService
from repositories.profilerepository import Profile


class Account:
    """UI component view for creating and selecting profiles
    """

    def __init__(self, root, handle_login, handle_profile, user):
        """initializes the account components variables

        Args:
            root (Tk): tkinter root window
            handle_login (any): handles log in window initialization
            handle_profile (any): handles profile window initialization
            user (any): the sessions logged in user
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_profile = handle_profile
        self._frame = None
        self._app = FinanceService()
        self._profile_tree = None
        self._profile = None
        self._user = user
        self._initialize()

    def pack(self):
        """packs the tkinter view component
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """destroy the tkinter frame
        """
        self._frame.destroy()

    def on_click(self, event):
        """handles the on click event of the tkinter treeview table

        Args:
            event (any): the click event

        Returns:
            any: the click event
        """
        item = self._profile_tree.selection()[0]
        if item:
            profile_name = self._profile_tree.item(item, "values")[0]
            get_profile = self._app.find_profile(profile_name)
            if get_profile:
                self._profile = get_profile
                self._handle_profile(self._profile)

        return event

    def create_profile(self, new_profile_entry):
        """handler for the creation of a profile, inserts a new profile in to the
        treeview if succesful

        Args:
            new_profile_entry (ttk.Entry): the profile name entry
        """
        profile_name = new_profile_entry.get()
        if profile_name != "":
            self._profile = self._app.create_profile(
                profile_name, self._user.username)
            if isinstance(self._profile, Profile):
                self._profile_tree.insert("", "end", values=self._profile.name)
                new_profile_entry.delete(0, "end")
            else:
                ttk.Label(master=self._frame, text=self._profile).grid(
                    row=5, columnspan=2)

    def _initialize(self):
        """initializes the tkinter components of the view
        """
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Welcome to Finanssit!",
                          font=("TkDefaultFont", 20))

        ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._handle_login
        ).grid(row=0, column=1, padx=5, pady=5)

        profiles_separator = ttk.Separator(
            master=self._frame, orient="horizontal")
        profiles_label = ttk.Label(master=self._frame, text="List of profiles",
                                   font=("Arial", 16))

        self._profile_tree = ttk.Treeview(master=self._frame, columns='Name',
                                          show='headings')

        new_profile_entry = ttk.Entry(master=self._frame)

        create_profile_button = ttk.Button(
            master=self._frame,
            text="Create profile",
            command=lambda: self.create_profile(new_profile_entry)
        )
        self._profile_tree.heading('Name', text='Name')

        label.grid(row=0, column=0, padx=5, pady=5)

        profiles_separator.grid(row=1, columnspan=2, sticky="ew", pady=10)
        profiles_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self._profile_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        new_profile_entry.grid(row=4, column=0, padx=5, pady=5)
        create_profile_button.grid(row=4, column=1, padx=5, pady=5)

        db_profiles = self._app.return_profiles(self._user.username)
        for profile in db_profiles:
            self._profile_tree.insert("", "end", values=profile.name)

        self._profile_tree.bind("<Double-1>", self.on_click)
