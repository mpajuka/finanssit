from tkinter import Tk, ttk, constants, Message
from register import Register
from login import Login
from account import Account


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
    
    def _handle_account_view(self):
        self._show_account()
           
    def _show_register(self):
        self._hide_current_view()
        
        self._current_view = Register(self._root, self._handle_login_view)
        
        self._current_view.pack()

    def _show_login(self):
        self._hide_current_view()
        
        self._current_view = Login(self._root, self._handle_register_view, self._handle_account_view)
        
        self._current_view.pack()
        
        
    def _show_account(self):
        self._hide_current_view()
        
        self._current_view = Account(self._root, self._handle_login_view)
        
        self._current_view.pack()
        
    def start(self):
        self._show_login()
    
    
            

    

    
        
window = Tk()
window.title("Finanssit")

ui = UI(window)
ui.start()

window.mainloop()