from tkinter import Tk
from app.calculadora import Calculadora

if __name__ == '__main__':
    main = Tk()
    root = Calculadora(main)
    root.start()
