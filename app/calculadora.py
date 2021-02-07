import tkinter
from .calculador import calcular


def add_screen(bnt_press, screen):
    value = screen.get()
    if value != 'Error':
        valor = screen.get()
        valor += bnt_press
        screen.set(valor)


def remove(screen):
    if screen.get() != 'Error':
        valor = screen.get()[:-1]
        screen.set(valor)


def interface(root):
    root.title('Calulcadora Tk')
    root.resizable(width=False, height=False)

    new_menu = tkinter.Menu(root)
    option_menu = tkinter.Menu(new_menu, tearoff=0)
    option_menu.add_separator()
    option_menu.add_command(label='Exit', command=lambda: sair(root))
    new_menu.add_cascade(label='Option', menu=option_menu)
    root.config(menu=new_menu)

    screen = tkinter.StringVar()

    input_screen = tkinter.Entry(root, font='Arial 20', bd=2, relief='solid', justify='right',
                                 width=18, textvariable=screen, exportselection=0)

    bnt_square_root = tkinter.Button(root, font='Arial 20', width=4, text='√', command=lambda: add_screen('√', screen))
    bnt_exponent = tkinter.Button(root, font='Arial 20', width=4, text='x²', command=lambda: add_screen('^', screen))
    bnt_clear = tkinter.Button(root, font='Arial 20', width=4, text='C', command=lambda: screen.set(''))
    bnt_delete = tkinter.Button(root, font='Arial 20', width=4, text='<-', command=lambda: remove(screen))

    bnt_9 = tkinter.Button(root, font='Arial 20', width=4, text=9, command=lambda: add_screen('9', screen))
    bnt_8 = tkinter.Button(root, font='Arial 20', width=4, text=8, command=lambda: add_screen('8', screen))
    bnt_7 = tkinter.Button(root, font='Arial 20', width=4, text=7, command=lambda: add_screen('7', screen))
    bnt_division = tkinter.Button(root, font='Arial 20', width=4, text='/', command=lambda: add_screen('/', screen))

    bnt_6 = tkinter.Button(root, font='Arial 20', width=4, text=6, command=lambda: add_screen('6', screen))
    bnt_5 = tkinter.Button(root, font='Arial 20', width=4, text=5, command=lambda: add_screen('5', screen))
    bnt_4 = tkinter.Button(root, font='Arial 20', width=4, text=4, command=lambda: add_screen('4', screen))
    bnt_times = tkinter.Button(root, font='Arial 20', width=4, text='X', command=lambda: add_screen('x', screen))

    bnt_3 = tkinter.Button(root, font='Arial 20', width=4, text=3, command=lambda: add_screen('3', screen))
    bnt_2 = tkinter.Button(root, font='Arial 20', width=4, text=2, command=lambda: add_screen('2', screen))
    bnt_1 = tkinter.Button(root, font='Arial 20', width=4, text=1, command=lambda: add_screen('1', screen))
    bnt_minus = tkinter.Button(root, font='Arial 20', width=4, text='-', command=lambda: add_screen('-', screen))

    bnt_dot = tkinter.Button(root, font='Arial 20', width=4, text='.', command=lambda: add_screen('.', screen))
    bnt_0 = tkinter.Button(root, font='Arial 20', width=4, text=0, command=lambda: add_screen('0', screen))
    bnt_equal = tkinter.Button(root, font='Arial 20', width=4, text='=', command=lambda: calcular(screen))
    bnt_plus = tkinter.Button(root, font='Arial 20', width=4, text='+', command=lambda: add_screen('+', screen))

    input_screen.grid(row=0, columnspan=4, sticky='we')

    bnt_square_root.grid(row=1, column=0)
    bnt_exponent.grid(row=1, column=1)
    bnt_clear.grid(row=1, column=2)
    bnt_delete.grid(row=1, column=3)

    bnt_9.grid(row=2, column=2)
    bnt_8.grid(row=2, column=1)
    bnt_7.grid(row=2, column=0)
    bnt_division.grid(row=2, column=3)

    bnt_6.grid(row=3, column=2)
    bnt_5.grid(row=3, column=1)
    bnt_4.grid(row=3, column=0)
    bnt_times.grid(row=3, column=3)

    bnt_3.grid(row=4, column=2)
    bnt_2.grid(row=4, column=1)
    bnt_1.grid(row=4, column=0)
    bnt_minus.grid(row=4, column=3)

    bnt_dot.grid(row=5, column=0)
    bnt_0.grid(row=5, column=1)
    bnt_equal.grid(row=5, column=2)
    bnt_plus.grid(row=5, column=3)


def sair(root):
    root.destroy()


def start(root):
    root.mainloop()
