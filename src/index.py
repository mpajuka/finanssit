from tkinter import Tk
from gui.ui import UI


def main():
    window = Tk()
    window.title("Finanssit")
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()
