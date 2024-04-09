from tkinter import Tk
from ui import UI

def main():
    window = Tk()
    window.title("Finanssit")
    
    ui = UI()
    ui.start()
    window.mainloop() 

if __name__ == "__main__":
    main()