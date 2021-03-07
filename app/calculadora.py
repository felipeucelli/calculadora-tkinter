# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
import tkinter
import json
from functools import partial

# Módulos próprios
from .calculador import Calculador
from .historic import Historic


class Calculadora:
    """
    Classe para a criação do layout, distribuição e adição de funcionalidade dos botões.
    """

    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora Tk')
        self.root.resizable(width=False, height=False)

        self.screen = tkinter.StringVar()
        self.control = tkinter.StringVar()
        self.calculate = Calculador(self.screen, self.control)
        self.historic = Historic()

        # Funções de inicialização
        self._create_menu()
        self._load_themes()
        self._interface()

        # Seta o background color do root
        self.root['bg'] = self.config['root']['bg']

    @staticmethod
    def load_theme_settings():
        """
        Responsável por carregar o arquivo "setting.json"
        :return: Retorna um dicionário das propriedades em "setting.json"
        """
        with open('app/setting.json', 'r') as settings:
            settings = json.load(settings)
        return settings

    def apply_theme(self, theme='dark'):
        """
        Responsável por definir o tema ativo
        :param theme: Tema selecionado, padrão Dark
        :return:
        """
        self.settings['active_theme'] = theme
        with open('app/setting.json', 'w') as file:
            json.dump(self.settings, file, indent=4)

    def _load_themes(self):
        """
        Responsável por carregar e selecionar os temas disponíveis no menu de opções
        :return:
        """
        self.settings = self.load_theme_settings()
        self.config = self.settings['themes']
        self.config = self.config[self.settings['active_theme']]
        for theme_name in self.settings["options"]:
            self.option_theme.add_command(label=theme_name, command=partial(self.apply_theme, theme_name))

    def add_screen(self, bnt_press):
        """
        Responsável por adicionar novos inputs
        :param bnt_press: Captura do bottom precionado
        :return:
        """

        # Verifica se o input está travado ou se ocorreu algum erro, caso contrário, adiciona o valor de input
        if self.screen.get() != 'Error' and 'e' not in self.screen.get():
            value = self.screen.get()
            value += bnt_press
            self.screen.set(value)

        # Formata o input se o mesmo for maior que 16 digitos
        if len(self.screen.get()) > 16:
            self.screen.set(self.screen.get()[:-1])

    def remove(self):
        """
        Responsável por remover o último valor digitado
        :return:
        """
        if self.screen.get() != 'Error' and 'e' not in self.screen.get():
            valor = self.screen.get()[:-1]
            self.screen.set(valor)

    def clear(self):
        """
        Responsável pela remoção de todos os valores no input
        :return:
        """
        self.control.set('')
        self.screen.set('')

    def input_control(self, *args):
        """
        Verifica se o input é um parâmetro válido
        :param args:
        :return:
        """
        _none = args
        _none = None

        # Verifica se o valor total é diferente do valor de controle
        if self.control.get() != '':
            if self.screen.get() != self.control.get():
                self.screen.set(self.control.get())

        # Verifica se o valor de entrada é válido e faz as devidas alterações
        if len(self.screen.get()) > 0 and 'E' not in self.screen.get() and 'ror' not in self.screen.get():
            for v in self.screen.get():
                if 'e' not in self.screen.get():
                    if not v.isalpha() or v == 'x':
                        self.screen.set(self.screen.get())
                    else:
                        self.screen.set(self.screen.get().replace(v, ''))
                if v == 'e' and self.control.get() == '':
                    self.screen.set(self.screen.get().replace(v, ''))
        elif 'E' in self.screen.get() or 'ror' in self.screen.get():
            self.screen.set('Error')

    def _create_menu(self):
        """
        Responsável por instanciar o menu na interface
        :return:
        """
        self.new_menu = tkinter.Menu(self.root)
        self.option_menu = tkinter.Menu(self.new_menu, tearoff=0)
        self.option_theme = tkinter.Menu(self.option_menu, tearoff=0)
        self.option_menu.add_command(label='Historic',
                                     command=lambda: self.historic.open_historic(self.screen, self.config))
        self.option_menu.add_cascade(label='Themes', menu=self.option_theme)
        self.option_menu.add_separator()
        self.option_menu.add_command(label='Exit', command=lambda: self.sair())
        self.new_menu.add_cascade(label='Options', menu=self.option_menu)
        self.root.config(menu=self.new_menu)

    def _interface(self):
        """
        Instânciação e configurações dos botões
        :return:
        """

        # Verifica os valores de entrada no input
        self.screen.trace('w', self.input_control)

        # Instânciação da área de input
        # Linha 0
        self.input_screen = tkinter.Entry(self.root, textvariable=self.screen, exportselection=0,
                                          cnf=[self.config['input']])

        # Seta o foco para o input
        self.input_screen.focus()

        # Instânciação dos botões númericos e operadores aritméticos
        # Linha 1
        self.btn_square_root = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='√')
        self.btn_exponent = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='x²')
        self.btn_clear = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='C')
        self.btn_delete = tkinter.Button(self.root, cnf=[self.config['btn_delete']], text='<-')

        # Linha 2
        self.btn_factorial = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='!')
        self.btn_open_parentheses = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='(')
        self.btn_close_parentheses = tkinter.Button(self.root, cnf=[self.config['btn_op']], text=')')
        self.btn_percentage = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='%')

        # Linha 3
        self.btn_9 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=9)
        self.btn_8 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=8)
        self.btn_7 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=7)
        self.btn_division = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='/')

        # Linha 4
        self.btn_6 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=6)
        self.btn_5 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=5)
        self.btn_4 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=4)
        self.btn_times = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='X')

        # Linha 5
        self.btn_3 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=3)
        self.btn_2 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=2)
        self.btn_1 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=1)
        self.btn_minus = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='-')

        # Linha 6
        self.btn_dot = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='.')
        self.btn_0 = tkinter.Button(self.root, cnf=[self.config['btn_num']], text=0)
        self.btn_equal = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='=')
        self.btn_plus = tkinter.Button(self.root, cnf=[self.config['btn_op']], text='+')

        # Eventos dos botões
        # Linha 1
        self.btn_factorial['command'] = lambda: self.add_screen('!')
        self.btn_open_parentheses['command'] = lambda: self.add_screen('(')
        self.btn_close_parentheses['command'] = lambda: self.add_screen(')')
        self.btn_percentage['command'] = lambda: self.add_screen('%')

        # Linha 2
        self.btn_square_root['command'] = lambda: self.add_screen('√')
        self.btn_exponent['command'] = lambda: self.add_screen('^')
        self.btn_clear['command'] = lambda: self.clear()
        self.btn_delete['command'] = lambda: self.remove()

        # Linha 3
        self.btn_9['command'] = lambda: self.add_screen('9')
        self.btn_8['command'] = lambda: self.add_screen('8')
        self.btn_7['command'] = lambda: self.add_screen('7')
        self.btn_division['command'] = lambda: self.add_screen('/')

        # Linha 4
        self.btn_6['command'] = lambda: self.add_screen('6')
        self.btn_5['command'] = lambda: self.add_screen('5')
        self.btn_4['command'] = lambda: self.add_screen('4')
        self.btn_times['command'] = lambda: self.add_screen('x')

        # Linha 5
        self.btn_3['command'] = lambda: self.add_screen('3')
        self.btn_2['command'] = lambda: self.add_screen('2')
        self.btn_1['command'] = lambda: self.add_screen('1')
        self.btn_minus['command'] = lambda: self.add_screen('-')

        # Linha 6
        self.btn_dot['command'] = lambda: self.add_screen('.')
        self.btn_0['command'] = lambda: self.add_screen('0')
        self.btn_equal['command'] = lambda: self.calculate.math_operation()
        self.btn_plus['command'] = lambda: self.add_screen('+')

        # Distribuição dos botões com o gerenciador de layout grid()
        # Linha 0
        self.input_screen.grid(row=0, columnspan=4, sticky='we')

        # Linha 1
        self.btn_square_root.grid(row=1, column=0, pady=1, padx=1)
        self.btn_exponent.grid(row=1, column=1, pady=1, padx=1)
        self.btn_clear.grid(row=1, column=2, pady=1, padx=1)
        self.btn_delete.grid(row=1, column=3, pady=1, padx=1)

        # Linha 2
        self.btn_factorial.grid(row=2, column=0, pady=1, padx=1)
        self.btn_open_parentheses.grid(row=2, column=1, pady=1, padx=1)
        self.btn_close_parentheses.grid(row=2, column=2, pady=1, padx=1)
        self.btn_percentage.grid(row=2, column=3, pady=1, padx=1)

        # Linha 3
        self.btn_9.grid(row=3, column=2, pady=1, padx=1)
        self.btn_8.grid(row=3, column=1, pady=1, padx=1)
        self.btn_7.grid(row=3, column=0, pady=1, padx=1)
        self.btn_division.grid(row=3, column=3, pady=1, padx=1)

        # Linha 4
        self.btn_6.grid(row=4, column=2, pady=1, padx=1)
        self.btn_5.grid(row=4, column=1, pady=1, padx=1)
        self.btn_4.grid(row=4, column=0, pady=1, padx=1)
        self.btn_times.grid(row=4, column=3, pady=1, padx=1)

        # Linha 5
        self.btn_3.grid(row=5, column=2, pady=1, padx=1)
        self.btn_2.grid(row=5, column=1, pady=1, padx=1)
        self.btn_1.grid(row=5, column=0, pady=1, padx=1)
        self.btn_minus.grid(row=5, column=3, pady=1, padx=1)

        # Linha 6
        self.btn_dot.grid(row=6, column=0, pady=1, padx=1)
        self.btn_0.grid(row=6, column=1, pady=1, padx=1)
        self.btn_equal.grid(row=6, column=2, pady=1, padx=1)
        self.btn_plus.grid(row=6, column=3, pady=1, padx=1)

    def sair(self):
        """
        Responsável por finalizar a aplicação
        :return:
        """
        self.root.destroy()

    def start(self):
        """
        Responsável por inicializar a aplicação
        :return:
        """
        self.root.mainloop()
