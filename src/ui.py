from tkinter import Tk, ttk, constants, Message
from register import Register
from login import Login


class UI:
    def __init__(self, root):
        self._root = root
        self._username = None
        self._password = None
        self._notification = None
        self._current_view = None
        
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
        
    def _handle_login_view(self):
        self._show_login()
        
    def _handle_register_view(self):
        self._show_register()
        
        
    def _show_register(self):
        self._hide_current_view()
        
        self._current_view = Register(self._root, self._handle_login_view)
        
        self._current_view.pack()

    def _show_login(self):
        self._hide_current_view()
        
        self._current_view = Login(self._root, self._handle_register_view)
        
        self._current_view.pack()
        
        
    def start(self):
        self._show_login()
        
            

    

    
        
window = Tk()
window.title("Finanssit")

ui = UI(window)
ui.start()

window.mainloop()


if user == None:
    print("A user with the credentials provided was not found.")
    newUserPrompt = input("Would you like to create a new user? (y/n): ")
    if newUserPrompt == "y":
        usePrevCred = input(
            "Would you like create the user with " +
            "the same credentials as you have given? (y/n): "
        )
        if usePrevCred == "y":
            newUser = app.register(username, hashed_password)
        else:
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            newUser = app.register(username, hashed_password)
        if newUser != None:
            print("New user successfully created!")
            user = app.login(username, password)
    else:
        print("Farewell!")
print(f"Welcome to Finanssit {user.username}!")