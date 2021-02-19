import tkinter
from .calculador import math_operation
from .historic import open_historic


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora Tk')
        self.root.resizable(width=False, height=False)

        self.screen = tkinter.StringVar()
        self.control = tkinter.StringVar()

        self._interface()
        self._create_menu()

    def add_screen(self, bnt_press):
        if self.screen.get() != 'Error' and 'e' not in self.screen.get():
            value = self.screen.get()
            value += bnt_press
            self.screen.set(value)
        if len(self.screen.get()) > 16:
            self.screen.set(self.screen.get()[:-1])

    def remove(self):
        if self.screen.get() != 'Error' and 'e' not in self.screen.get():
            valor = self.screen.get()[:-1]
            self.screen.set(valor)

    def clear(self):
        self.screen.set('')
        self.control.set('')

    def input_control(self, *args):
        _none = args
        _none = None
        if len(self.screen.get()) > 0 and 'E' not in self.screen.get() and 'ror' not in self.screen.get():
            for v in self.screen.get():
                if 'e' not in self.screen.get():
                    if not v.isalpha() or v == 'x':
                        self.screen.set(self.screen.get())
                    else:
                        value = self.screen.get().replace(v, '')
                        self.screen.set(value)
                else:
                    if self.screen.get() != self.control.get():
                        self.screen.set(self.control.get())
        elif 'E' in self.screen.get() or 'ror' in self.screen.get():
            self.screen.set('Error')
        if len(self.screen.get()) > 15 and self.screen.get()[len(self.screen.get()) - 1] != 'e':
            self.screen.set(self.screen.get()[:-1])

    def _create_menu(self):
        self.new_menu = tkinter.Menu(self.root)
        self.option_menu = tkinter.Menu(self.new_menu, tearoff=0)
        self.option_menu.add_command(label='Historic', command=lambda: open_historic(screen=self.screen))
        self.option_menu.add_separator()
        self.option_menu.add_command(label='Exit', command=lambda: self.sair())
        self.new_menu.add_cascade(label='Options', menu=self.option_menu)
        self.root.config(menu=self.new_menu)

    def _interface(self):
        self.screen.trace('w', self.input_control)

        self.input_screen = tkinter.Entry(self.root, font='Arial 20', bd=1, relief='solid', justify='right',
                                          width=18, textvariable=self.screen, exportselection=0)
        self.input_screen.focus()

        self.btn_square_root = tkinter.Button(self.root, font='Arial 20', width=4, text='√')
        self.btn_exponent = tkinter.Button(self.root, font='Arial 20', width=4, text='x²')
        self.btn_clear = tkinter.Button(self.root, font='Arial 20', width=4, text='C')
        self.btn_delete = tkinter.Button(self.root, font='Arial 20', width=4, text='<-')

        self.btn_factorial = tkinter.Button(self.root, font='Arial 20', width=4, text='!')
        self.btn_open_parentheses = tkinter.Button(self.root, font='Arial 20', width=4, text='(')
        self.btn_close_parentheses = tkinter.Button(self.root, font='Arial 20', width=4, text=')')
        self.btn_percentage = tkinter.Button(self.root, font='Arial 20', width=4, text='%')

        self.btn_9 = tkinter.Button(self.root, font='Arial 20', width=4, text=9)
        self.btn_8 = tkinter.Button(self.root, font='Arial 20', width=4, text=8)
        self.btn_7 = tkinter.Button(self.root, font='Arial 20', width=4, text=7)
        self.btn_division = tkinter.Button(self.root, font='Arial 20', width=4, text='/')

        self.btn_6 = tkinter.Button(self.root, font='Arial 20', width=4, text=6)
        self.btn_5 = tkinter.Button(self.root, font='Arial 20', width=4, text=5)
        self.btn_4 = tkinter.Button(self.root, font='Arial 20', width=4, text=4)
        self.btn_times = tkinter.Button(self.root, font='Arial 20', width=4, text='X')

        self.btn_3 = tkinter.Button(self.root, font='Arial 20', width=4, text=3)
        self.btn_2 = tkinter.Button(self.root, font='Arial 20', width=4, text=2)
        self.btn_1 = tkinter.Button(self.root, font='Arial 20', width=4, text=1)
        self.btn_minus = tkinter.Button(self.root, font='Arial 20', width=4, text='-')

        self.btn_dot = tkinter.Button(self.root, font='Arial 20', width=4, text='.')
        self.btn_0 = tkinter.Button(self.root, font='Arial 20', width=4, text=0)
        self.btn_equal = tkinter.Button(self.root, font='Arial 20', width=4, text='=')
        self.btn_plus = tkinter.Button(self.root, font='Arial 20', width=4, text='+')

        self.btn_factorial['command'] = lambda: self.add_screen('!')
        self.btn_open_parentheses['command'] = lambda: self.add_screen('(')
        self.btn_close_parentheses['command'] = lambda: self.add_screen(')')
        self.btn_percentage['command'] = lambda: self.add_screen('%')

        self.btn_square_root['command'] = lambda: self.add_screen('√')
        self.btn_exponent['command'] = lambda: self.add_screen('^')
        self.btn_clear['command'] = lambda: self.clear()
        self.btn_delete['command'] = lambda: self.remove()

        self.btn_9['command'] = lambda: self.add_screen('9')
        self.btn_8['command'] = lambda: self.add_screen('8')
        self.btn_7['command'] = lambda: self.add_screen('7')
        self.btn_division['command'] = lambda: self.add_screen('/')

        self.btn_6['command'] = lambda: self.add_screen('6')
        self.btn_5['command'] = lambda: self.add_screen('5')
        self.btn_4['command'] = lambda: self.add_screen('4')
        self.btn_times['command'] = lambda: self.add_screen('x')

        self.btn_3['command'] = lambda: self.add_screen('3')
        self.btn_2['command'] = lambda: self.add_screen('2')
        self.btn_1['command'] = lambda: self.add_screen('1')
        self.btn_minus['command'] = lambda: self.add_screen('-')

        self.btn_dot['command'] = lambda: self.add_screen('.')
        self.btn_0['command'] = lambda: self.add_screen('0')
        self.btn_equal['command'] = lambda: math_operation(self.screen, self.control)
        self.btn_plus['command'] = lambda: self.add_screen('+')

        self.input_screen.grid(row=0, columnspan=4, sticky='we')

        self.btn_square_root.grid(row=1, column=0)
        self.btn_exponent.grid(row=1, column=1)
        self.btn_clear.grid(row=1, column=2)
        self.btn_delete.grid(row=1, column=3)

        self.btn_factorial.grid(row=2, column=0)
        self.btn_open_parentheses.grid(row=2, column=1)
        self.btn_close_parentheses.grid(row=2, column=2)
        self.btn_percentage.grid(row=2, column=3)

        self.btn_9.grid(row=3, column=2)
        self.btn_8.grid(row=3, column=1)
        self.btn_7.grid(row=3, column=0)
        self.btn_division.grid(row=3, column=3)

        self.btn_6.grid(row=4, column=2)
        self.btn_5.grid(row=4, column=1)
        self.btn_4.grid(row=4, column=0)
        self.btn_times.grid(row=4, column=3)

        self.btn_3.grid(row=5, column=2)
        self.btn_2.grid(row=5, column=1)
        self.btn_1.grid(row=5, column=0)
        self.btn_minus.grid(row=5, column=3)

        self.btn_dot.grid(row=6, column=0)
        self.btn_0.grid(row=6, column=1)
        self.btn_equal.grid(row=6, column=2)
        self.btn_plus.grid(row=6, column=3)

    def sair(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()
