from tkinter import Tk
from gui.ui import UI


def main():
    """_summary_
    """    
    window = Tk()
    window.eval('tk::PlaceWindow . center')

    window.title("Finanssit")
    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
