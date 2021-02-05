import tkinter
# import math


def calcular():
    pass


def add_screen(bnt_press):
    valor = screen.get()
    valor += bnt_press
    screen.set(valor)


def remove():
    valor = screen.get()[0:-1]
    screen.set(valor)


def wipe():
    screen.set('')


root = tkinter.Tk()
root.title('Calulcadora')
root.geometry('296x318')
root.resizable(width=False, height=False)

screen = tkinter.StringVar()

label_screen = tkinter.Label(root, font='Arial 20', width=18,
                             textvariable=screen, anchor='e'
                             ).grid(row=0, columnspan=4)


square = tkinter.Button(root, font='Arial 20', width=4, text='√',
                        command=lambda: add_screen('√')
                        ).grid(row=1, column=0)

expo = tkinter.Button(root, font='Arial 20', width=4, text='x²',
                      command=lambda: add_screen('^')
                      ).grid(row=1, column=1)

clear = tkinter.Button(root, font='Arial 20', width=4, text='C',
                       command=wipe
                       ).grid(row=1, column=2)

delete = tkinter.Button(root, font='Arial 20', width=4, text='<-',
                        command=remove
                        ).grid(row=1, column=3)

bnt9 = tkinter.Button(root, font='Arial 20', width=4, text='9',
                      command=lambda: add_screen('9')
                      ).grid(row=2, column=2)

bnt8 = tkinter.Button(root, font='Arial 20', width=4, text='8',
                      command=lambda: add_screen('8')
                      ).grid(row=2, column=1)

bnt7 = tkinter.Button(root, font='Arial 20', width=4, text='7',
                      command=lambda: add_screen('7')
                      ).grid(row=2, column=0)

div = tkinter.Button(root, font='Arial 20', width=4, text='/',
                     command=lambda: add_screen('/')
                     ).grid(row=2, column=3)

bnt6 = tkinter.Button(root, font='Arial 20', width=4, text='6',
                      command=lambda: add_screen('6')
                      ).grid(row=3, column=2)

bnt5 = tkinter.Button(root, font='Arial 20', width=4, text='5',
                      command=lambda: add_screen('5')
                      ).grid(row=3, column=1)

bnt4 = tkinter.Button(root, font='Arial 20', width=4, text='4',
                      command=lambda: add_screen('4')
                      ).grid(row=3, column=0)

times = tkinter.Button(root, font='Arial 20', width=4, text='X',
                       command=lambda: add_screen('x')
                       ).grid(row=3, column=3)

bnt3 = tkinter.Button(root, font='Arial 20', width=4, text='3',
                      command=lambda: add_screen('3')
                      ).grid(row=4, column=2)

bnt2 = tkinter.Button(root, font='Arial 20', width=4, text='2',
                      command=lambda: add_screen('2')
                      ).grid(row=4, column=1)

bnt1 = tkinter.Button(root, font='Arial 20', width=4, text='1',
                      command=lambda: add_screen('1')
                      ).grid(row=4, column=0)

minus = tkinter.Button(root, font='Arial 20', width=4, text='-',
                       command=lambda: add_screen('-')
                       ).grid(row=4, column=3)

dot = tkinter.Button(root, font='Arial 20', width=4, text='.',
                     command=lambda: add_screen('.')
                     ).grid(row=5, column=0)

bnt0 = tkinter.Button(root, font='Arial 20', width=4, text='0',
                      command=lambda: add_screen('0')
                      ).grid(row=5, column=1)

equal = tkinter.Button(root, font='Arial 20', width=4, text='=',
                       command=calcular
                       ).grid(row=5, column=2)

plus = tkinter.Button(root, font='Arial 20', width=4, text='+',
                      command=lambda: add_screen('+')
                      ).grid(row=5, column=3)

root.mainloop()
