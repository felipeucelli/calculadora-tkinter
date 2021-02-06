import tkinter
from math import sqrt


def calculate():
    screen_tot = screen.get()
    if len(screen_tot) > 1 and screen_tot[0] != '+' and screen_tot[0] != '-' and screen_tot[0] != 'x'\
            and screen_tot[0] != '/' and screen_tot[0] != '^' and screen_tot[0] != '.':
        if '+' in screen_tot and '√' not in screen_tot:
            if screen_tot.count('+') == 1:
                result = screen_tot.split('+')
                if result[1] != '':
                    result_screen = str(float(result[0]) + float(result[1]))
                    for c in result_screen.split('.')[1]:
                        if c != '0':
                            screen.set(str(result_screen))
                            break
                        else:
                            screen.set(str(result_screen.split('.')[0]))
            else:
                screen.set('Syntax invalidate')
        if '-' in screen_tot and '√' not in screen_tot:
            if screen_tot.count('-') == 1:
                result = screen_tot.split('-')
                if result[1] != '':
                    result_screen = str(float(result[0]) - float(result[1]))
                    for c in result_screen.split('.')[1]:
                        if c != '0':
                            screen.set(str(result_screen))
                            break
                    else:
                        screen.set(str(result_screen.split('.')[0]))
            else:
                screen.set('Syntax invalidate')
        if 'x' in screen_tot and '√' not in screen_tot:
            if screen_tot.count('x') == 1:
                result = screen_tot.split('x')
                if result[1] != '':
                    result_screen = str(float(result[0]) * float(result[1]))
                    for c in result_screen.split('.')[1]:
                        if c != '0':
                            screen.set(str(result_screen))
                            break
                        else:
                            screen.set(str(result_screen.split('.')[0]))
            else:
                screen.set('Syntax invalidate')
        if '/' in screen_tot and '√' not in screen_tot:
            if screen_tot.count('/') == 1:
                result = screen_tot.split('/')
                if result[1] != '':
                    result_screen = str(float(result[0]) / float(result[1]))
                    for c in result_screen.split('.')[1]:
                        if c != '0':
                            screen.set(str(result_screen))
                            break
                        else:
                            screen.set(str(result_screen.split('.')[0]))
            else:
                screen.set('Syntax invalidate')
        if screen_tot[0] == '√' and '+' not in screen_tot and '-' not in screen_tot and 'x' not in screen_tot \
                and '/' not in screen_tot and '^' not in screen_tot and '.' not in screen_tot:
            if screen_tot.count('√') == 1:
                result = screen_tot.split('√')
                if result[1] != '':
                    result_screen = str(sqrt(float(result[1])))
                    for c in result_screen.split('.')[1]:
                        if c != '0':
                            screen.set(str(result_screen))
                            break
                        else:
                            screen.set(str(result_screen.split('.')[0]))
            else:
                screen.set('Syntax invalidate')
        if '^' in screen_tot and '√' not in screen_tot:
            if screen_tot.count('^') == 1:
                result = screen_tot.split('^')
                if result[1] != '':
                    result_screen = str(float(result[0]) ** float(result[1]))
                    for c in result_screen.split('.')[1]:
                        if c != '0':
                            screen.set(str(result_screen))
                            break
                        else:
                            screen.set(str(result_screen.split('.')[0]))
            else:
                screen.set('Syntax invalidate')


def add_screen(bnt_press):
    value = screen.get()
    if value != 'Syntax invalidate':
        valor = screen.get()
        valor += bnt_press
        screen.set(valor)


def remove():
    if screen.get() != 'Syntax invalidate':
        valor = screen.get()[0:-1]
        screen.set(valor)


root = tkinter.Tk()
root.title('Calulcadora Tk')
root.resizable(width=False, height=False)

screen = tkinter.StringVar()

label_screen = tkinter.Label(root, font='Arial 20', bd=2, relief='solid',
                             width=18, height=2, textvariable=screen, anchor='e')

square = tkinter.Button(root, font='Arial 20', width=4, text='√', command=lambda: add_screen('√'))
expo = tkinter.Button(root, font='Arial 20', width=4, text='x²', command=lambda: add_screen('^'))
clear = tkinter.Button(root, font='Arial 20', width=4, text='C', command=lambda: screen.set(''))
delete = tkinter.Button(root, font='Arial 20', width=4, text='<-', command=lambda: remove())

bnt9 = tkinter.Button(root, font='Arial 20', width=4, text='9', command=lambda: add_screen('9'))
bnt8 = tkinter.Button(root, font='Arial 20', width=4, text='8', command=lambda: add_screen('8'))
bnt7 = tkinter.Button(root, font='Arial 20', width=4, text='7', command=lambda: add_screen('7'))
div = tkinter.Button(root, font='Arial 20', width=4, text='/', command=lambda: add_screen('/'))

bnt6 = tkinter.Button(root, font='Arial 20', width=4, text='6', command=lambda: add_screen('6'))
bnt5 = tkinter.Button(root, font='Arial 20', width=4, text='5', command=lambda: add_screen('5'))
bnt4 = tkinter.Button(root, font='Arial 20', width=4, text='4', command=lambda: add_screen('4'))
times = tkinter.Button(root, font='Arial 20', width=4, text='X', command=lambda: add_screen('x'))

bnt3 = tkinter.Button(root, font='Arial 20', width=4, text='3', command=lambda: add_screen('3'))
bnt2 = tkinter.Button(root, font='Arial 20', width=4, text='2', command=lambda: add_screen('2'))
bnt1 = tkinter.Button(root, font='Arial 20', width=4, text='1', command=lambda: add_screen('1'))
minus = tkinter.Button(root, font='Arial 20', width=4, text='-', command=lambda: add_screen('-'))

dot = tkinter.Button(root, font='Arial 20', width=4, text='.', command=lambda: add_screen('.'))
bnt0 = tkinter.Button(root, font='Arial 20', width=4, text='0', command=lambda: add_screen('0'))
equal = tkinter.Button(root, font='Arial 20', width=4, text='=', command=lambda: calculate())
plus = tkinter.Button(root, font='Arial 20', width=4, text='+', command=lambda: add_screen('+'))

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

root.mainloop()
