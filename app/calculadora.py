import tkinter
from .calculador import calcular


def add_screen(bnt_press, screen):
    value = screen.get()
    if value != 'Syntax invalidate':
        valor = screen.get()
        valor += bnt_press
        screen.set(valor)


def remove(screen):
    if screen.get() != 'Syntax invalidate':
        valor = screen.get()[0:-1]
        screen.set(valor)


def interface(root):
    root.title('Calulcadora Tk')
    root.resizable(width=False, height=False)

    screen = tkinter.StringVar()

    label_screen = tkinter.Entry(root, font='Arial 20', bd=2, relief='solid', justify='right',
                                 width=18, textvariable=screen, exportselection=0)

    square = tkinter.Button(root, font='Arial 20', width=4, text='√', command=lambda: add_screen('√', screen))
    expo = tkinter.Button(root, font='Arial 20', width=4, text='x²', command=lambda: add_screen('^', screen))
    clear = tkinter.Button(root, font='Arial 20', width=4, text='C', command=lambda: screen.set(''))
    delete = tkinter.Button(root, font='Arial 20', width=4, text='<-', command=lambda: remove(screen))

    bnt9 = tkinter.Button(root, font='Arial 20', width=4, text='9', command=lambda: add_screen('9', screen))
    bnt8 = tkinter.Button(root, font='Arial 20', width=4, text='8', command=lambda: add_screen('8', screen))
    bnt7 = tkinter.Button(root, font='Arial 20', width=4, text='7', command=lambda: add_screen('7', screen))
    div = tkinter.Button(root, font='Arial 20', width=4, text='/', command=lambda: add_screen('/', screen))

    bnt6 = tkinter.Button(root, font='Arial 20', width=4, text='6', command=lambda: add_screen('6', screen))
    bnt5 = tkinter.Button(root, font='Arial 20', width=4, text='5', command=lambda: add_screen('5', screen))
    bnt4 = tkinter.Button(root, font='Arial 20', width=4, text='4', command=lambda: add_screen('4', screen))
    times = tkinter.Button(root, font='Arial 20', width=4, text='X', command=lambda: add_screen('x', screen))

    bnt3 = tkinter.Button(root, font='Arial 20', width=4, text='3', command=lambda: add_screen('3', screen))
    bnt2 = tkinter.Button(root, font='Arial 20', width=4, text='2', command=lambda: add_screen('2', screen))
    bnt1 = tkinter.Button(root, font='Arial 20', width=4, text='1', command=lambda: add_screen('1', screen))
    minus = tkinter.Button(root, font='Arial 20', width=4, text='-', command=lambda: add_screen('-', screen))

    dot = tkinter.Button(root, font='Arial 20', width=4, text='.', command=lambda: add_screen('.', screen))
    bnt0 = tkinter.Button(root, font='Arial 20', width=4, text='0', command=lambda: add_screen('0', screen))
    equal = tkinter.Button(root, font='Arial 20', width=4, text='=', command=lambda: calcular(screen))
    plus = tkinter.Button(root, font='Arial 20', width=4, text='+', command=lambda: add_screen('+', screen))

    label_screen.grid(row=0, columnspan=4, sticky='we')

    square.grid(row=1, column=0)
    expo.grid(row=1, column=1)
    clear.grid(row=1, column=2)
    delete.grid(row=1, column=3)

    bnt9.grid(row=2, column=2)
    bnt8.grid(row=2, column=1)
    bnt7.grid(row=2, column=0)
    div.grid(row=2, column=3)

    bnt6.grid(row=3, column=2)
    bnt5.grid(row=3, column=1)
    bnt4.grid(row=3, column=0)
    times.grid(row=3, column=3)

    bnt3.grid(row=4, column=2)
    bnt2.grid(row=4, column=1)
    bnt1.grid(row=4, column=0)
    minus.grid(row=4, column=3)

    dot.grid(row=5, column=0)
    bnt0.grid(row=5, column=1)
    equal.grid(row=5, column=2)
    plus.grid(row=5, column=3)


def start(root):
    root.mainloop()
