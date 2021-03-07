# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
from tkinter import Tk

# Módulo próprio
from lib.calculadora import Calculadora

if __name__ == '__main__':
    main = Tk()
    root = Calculadora(main)
    root.start()
