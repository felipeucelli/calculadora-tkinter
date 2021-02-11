import tkinter
from .calculador import math_operation
from .historic import open_historic


def add_screen(bnt_press, screen):
    value = screen.get()
    if value != 'Error':
        valor = screen.get()
        valor += bnt_press
        screen.set(valor)
    if len(value) > 17:
        screen.set(screen.get()[:-1])


def remove(screen):
    if screen.get() != 'Error':
        valor = screen.get()[:-1]
        screen.set(valor)


def interface(root):
    root.title('Calulcadora Tk')
    root.resizable(width=False, height=False)

    new_menu = tkinter.Menu(root)
    option_menu = tkinter.Menu(new_menu, tearoff=0)
    option_menu.add_command(label='Historic', command=lambda: open_historic(screen=screen))
    option_menu.add_separator()
    option_menu.add_command(label='Exit', command=lambda: sair(root))
    new_menu.add_cascade(label='Options', menu=option_menu)
    root.config(menu=new_menu)

    screen = tkinter.StringVar()

    input_screen = tkinter.Entry(root, font='Arial 20', bd=2, relief='solid', justify='right',
                                 width=18, textvariable=screen, exportselection=0)

    btn_square_root = tkinter.Button(root, font='Arial 20', width=4, text='√', command=lambda: add_screen('√', screen))
    btn_exponent = tkinter.Button(root, font='Arial 20', width=4, text='x²', command=lambda: add_screen('^', screen))
    btn_clear = tkinter.Button(root, font='Arial 20', width=4, text='C', command=lambda: screen.set(''))
    btn_delete = tkinter.Button(root, font='Arial 20', width=4, text='<-', command=lambda: remove(screen))

    btn_9 = tkinter.Button(root, font='Arial 20', width=4, text=9, command=lambda: add_screen('9', screen))
    btn_8 = tkinter.Button(root, font='Arial 20', width=4, text=8, command=lambda: add_screen('8', screen))
    btn_7 = tkinter.Button(root, font='Arial 20', width=4, text=7, command=lambda: add_screen('7', screen))
    btn_division = tkinter.Button(root, font='Arial 20', width=4, text='/', command=lambda: add_screen('/', screen))

    btn_6 = tkinter.Button(root, font='Arial 20', width=4, text=6, command=lambda: add_screen('6', screen))
    btn_5 = tkinter.Button(root, font='Arial 20', width=4, text=5, command=lambda: add_screen('5', screen))
    btn_4 = tkinter.Button(root, font='Arial 20', width=4, text=4, command=lambda: add_screen('4', screen))
    btn_times = tkinter.Button(root, font='Arial 20', width=4, text='X', command=lambda: add_screen('x', screen))

    btn_3 = tkinter.Button(root, font='Arial 20', width=4, text=3, command=lambda: add_screen('3', screen))
    btn_2 = tkinter.Button(root, font='Arial 20', width=4, text=2, command=lambda: add_screen('2', screen))
    btn_1 = tkinter.Button(root, font='Arial 20', width=4, text=1, command=lambda: add_screen('1', screen))
    btn_minus = tkinter.Button(root, font='Arial 20', width=4, text='-', command=lambda: add_screen('-', screen))

    btn_dot = tkinter.Button(root, font='Arial 20', width=4, text='.', command=lambda: add_screen('.', screen))
    btn_0 = tkinter.Button(root, font='Arial 20', width=4, text=0, command=lambda: add_screen('0', screen))
    btn_equal = tkinter.Button(root, font='Arial 20', width=4, text='=', command=lambda: math_operation(screen))
    btn_plus = tkinter.Button(root, font='Arial 20', width=4, text='+', command=lambda: add_screen('+', screen))

    input_screen.grid(row=0, columnspan=4, sticky='we')

    btn_square_root.grid(row=1, column=0)
    btn_exponent.grid(row=1, column=1)
    btn_clear.grid(row=1, column=2)
    btn_delete.grid(row=1, column=3)

    btn_9.grid(row=2, column=2)
    btn_8.grid(row=2, column=1)
    btn_7.grid(row=2, column=0)
    btn_division.grid(row=2, column=3)

    btn_6.grid(row=3, column=2)
    btn_5.grid(row=3, column=1)
    btn_4.grid(row=3, column=0)
    btn_times.grid(row=3, column=3)

    btn_3.grid(row=4, column=2)
    btn_2.grid(row=4, column=1)
    btn_1.grid(row=4, column=0)
    btn_minus.grid(row=4, column=3)

    btn_dot.grid(row=5, column=0)
    btn_0.grid(row=5, column=1)
    btn_equal.grid(row=5, column=2)
    btn_plus.grid(row=5, column=3)


def sair(root):
    root.destroy()


def start(root):
    root.mainloop()
