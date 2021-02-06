from tkinter import Tk
from app.calculadora import start, interface

if __name__ == '__main__':
    main = Tk()
    interface(main)
    start(main)
