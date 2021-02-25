# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
from math import sqrt, factorial

# Módulo próprio
from .historic import Historic


class Calculador:
    """
    Classe responsável por realizar todos os calculos da calculadora

    OBS: Poderia ser usado um bloco 'Try, except' para controle de fluxo, porém optei por tratar os possíveis erros
    """
    def __init__(self, screen, control):
        self.screen = screen
        self.control = control
        self.historic = Historic()

    def duplicate_analysis(self):
        """
        Responsável por verficar se há algum operador dublicado em sequência
        :return: 'True' se não houver operador duplicado, ou 'False' se houver
        """
        analysis = True
        for k, v in enumerate(self.screen.get()):
            if not v.isnumeric():
                if len(self.screen.get()) > k + 1:
                    if self.screen.get()[k + 1] == v:
                        analysis = False
                        break
        return analysis

    def validate_characters(self):
        """
        Responsável por verificar se os valores estão de acordo com uma operação aritmética
        :return: 'True' se os operadores estiverem de acordo, ou 'False' caso não estiverem
        """
        if self.duplicate_analysis():
            validate_expression = False
            for k, v in enumerate(self.screen.get()):
                if not v.isnumeric() and self.screen.get()[0] != '√' and \
                        self.screen.get()[len(self.screen.get()) - 1] != '!' or v == '.' or v == '(' or \
                        v == ')':

                    # Verifica se o ultimo valor do input é um número ou se é um operador válido
                    if self.screen.get()[len(self.screen.get()) - 1].isnumeric() or \
                            self.screen.get()[len(self.screen.get()) - 1] == ')' or \
                            self.screen.get()[len(self.screen.get()) - 1] == '%' or \
                            self.screen.get()[len(self.screen.get()) - 1] == '!':

                        # Verifica se o valor que precede o operador é válido
                        if len(self.screen.get()) > k + 1:
                            if self.screen.get()[k + 1].isnumeric() or self.screen.get()[k + 1] == '-' or \
                                    self.screen.get()[k + 1] == '(':
                                validate_expression = True
                            elif v == ')':
                                validate_expression = True
                            elif v == '!':
                                validate_expression = True
                            elif v == '.' and self.screen.get()[k + 1].isnumeric():
                                validate_expression = True
                            elif v == '%':
                                validate_expression = True
                            else:
                                validate_expression = False
                                break
                    else:
                        validate_expression = False
                        break
                else:
                    validate_expression = True
            if validate_expression:
                if '(' in self.screen.get() or ')' in self.screen.get():
                    if self.screen.get().count('(') == self.screen.get().count(')'):
                        all_ok = True
                    else:
                        all_ok = False
                else:
                    all_ok = True
            else:
                all_ok = False
        else:
            all_ok = False

        return all_ok

    def valid_operation(self):
        """
        Responsável por verificar o primeiro valor do input e se há algum valor alpha-numérico
        :return: 'True' se não houver valor alpha-numérico, ou 'False' caso houver
        """
        validate_symbols = False
        if self.screen.get()[0].isnumeric() or self.screen.get()[0] == '√' or self.screen.get()[0] == '-' or \
                self.screen.get()[0] == '(':
            for c in self.screen.get():
                if not c.isalpha() or c == 'x':
                    validate_symbols = True
                else:
                    validate_symbols = False
                    break
            if validate_symbols:
                return self.validate_characters()
            else:
                return False

    def basic_operation(self, entry=''):
        """
        Responsável por realizar operações aritméticas básícas
        :param entry: Valor a ser calculado caso não for possível calcular o input
        :return: Resultado da operação aritmética básica
        """
        if entry == '':
            return eval(self.screen.get())
        else:
            return eval(entry)

    def calculate_square_root(self):
        """
        Responsável por calcular uma raiz quadrada
        :return: Radiciação do input
        """
        if len(self.screen.get()) > 1:
            if self.screen.get().count('√') == 1 and self.screen.get()[1] != '-':
                if not self.screen.get().split('√')[1].isnumeric() and self.screen.get()[1].isnumeric():

                    # Efetua a fatoração no input e sua radiciação, caso houver necessidade
                    if '!' in self.screen.get():
                        if self.screen.get()[len(self.screen.get()) - 1] == '!':
                            screen_get_tot = sqrt(float(self.calculate_factorial(
                                self.screen.get().split('√')[1])))
                        else:
                            screen_get_tot = 'Error'

                    # Efetua a razão centesimal no input e sua radiciação, caso houver necessidade
                    elif '%' in self.screen.get():
                        if self.screen.get()[len(self.screen.get()) - 1] == '%':
                            screen_get_tot = sqrt(float(self.calculate_percentage(
                                self.screen.get().split('√')[1])))
                        else:
                            screen_get_tot = 'Error'

                    # Efetua uma operação aritmética básica no input e sua radiciação, caso houver necessidade
                    else:
                        square_root = self.basic_operation(self.screen.get().split('√')[1])
                        if str(square_root)[0] != '-':
                            screen_get_tot = sqrt(float(square_root))
                        else:
                            screen_get_tot = 'Error'

                # Efetua a radiciação do input
                else:
                    square_root = self.screen.get().split('√')[1]
                    screen_get_tot = sqrt(float(square_root))
            else:
                screen_get_tot = 'Error'
        else:
            screen_get_tot = 'Error'
        return screen_get_tot

    @staticmethod
    def calculate_factorial(screen):
        """
        Responsável por realizar a fatoração do input
        :param screen: Valor a se fatorado
        :return: Fatoração da entrada 'screen'
        """

        # Verifica se o input é um valor float
        factorial_ok = True
        if '.' in screen:
            for v in screen.split('.')[1]:
                if v != '0' and v != '!':
                    factorial_ok = False
                    break
                else:
                    screen = screen.split('.')[0]
                    factorial_ok = True
        else:
            factorial_ok = True

        if factorial_ok:

            # Seta o número de operações a serem realizadas
            if screen[len(screen) - 1] == '!':
                loop = len(screen.split('!')) - 1
            else:
                loop = len(screen.split('!'))

            # Seta o valor do último operador do input
            if screen[len(screen) - 1] == '!':
                last_fact = True
            else:
                last_fact = False
            i = 0
            fact_tot = ''
            while loop > 0:
                fact_1 = ''
                fact_2 = ''
                fact_3 = ''

                # Verifica se a primeira ação é uma operação básica ou uma fatoração
                if screen.split('!')[0].isnumeric() or screen.split('!')[0][0] == '-':

                    # Realiza a fatoração simples
                    if screen.split('!')[i].isnumeric():
                        fact_1 = str(factorial(int(screen.split('!')[i])))
                    else:

                        # Realiza a fatoração de valores que contenha operadores aritméticos básicos
                        if screen.split('!')[i][1:].isnumeric():
                            if loop == 1:
                                if last_fact:
                                    fact_3 = screen.split('!')[i][0]
                                    fact_3 += str(factorial(int(screen.split('!')[i][1:])))
                                else:
                                    fact_3 = screen.split('!')[i][0]
                                    fact_3 += str(eval(screen.split('!')[i][1:]))
                            else:
                                fact_2 = screen.split('!')[i][0]
                                fact_2 += str(factorial(int(screen.split('!')[i][1:])))
                        else:
                            fact_3 = screen.split('!')[i][0]
                            fact_3 += str(eval(screen.split('!')[i]))
                else:
                    screen = screen.replace(str(screen.split('!')[0]), str(eval(screen.split('!')[0])))
                    i -= 1
                    loop += 1

                fact_tot += str(fact_1) + str(fact_2) + str(fact_3)
                i += 1
                loop -= 1
            if '--' in fact_tot:
                fact_tot = fact_tot.replace('--', '-')
            return str(eval(fact_tot))
        else:
            return 'Error'

    @staticmethod
    def calculate_percentage(screen):
        """
        Responsável por realizar a razão centesimal do input
        :param screen: Valor a ser realizado a razão centesimal
        :return: Razão centesimal da entrada 'screen'
        """
        if not screen.split('%')[0].isnumeric():
            percentage_include = ''
            for v in screen:
                if v.isnumeric() or v == '%' or v == '.':
                    percentage_include += v
                else:
                    percentage_include = ''

            # Converte os valores de entrada para valores percentuais
            percentage_include = percentage_include.split('%')[0]
            first_value = screen.split(percentage_include + '%')[0]
            percentage_conversion = float(percentage_include) / 100
            convert_first_value = first_value[0:len(first_value) - 1]
            if not convert_first_value.isnumeric():
                operation_first_value = eval(convert_first_value)
                percentage_tot = float(operation_first_value) * float(percentage_conversion)
            else:
                percentage_tot = float(convert_first_value) * float(percentage_conversion)
            return eval(first_value + str(percentage_tot))
        else:
            return float(screen.split('%')[0]) / 100

    def convert_symbols(self):
        """
        Responsável por converter alguns símbolos para a interpretação do python
        :return: Valores convertidos para serem interpretados pelo python
        """

        # Converte o operador de exponenciação
        if '^' in self.screen.get():
            self.screen.set(self.screen.get().replace('^', '**'))

        # Converte o operador de multiplicação
        if 'x' in self.screen.get():
            self.screen.set(self.screen.get().replace('x', '*'))

        # Adiciona um operador de multiplicação antes do 'abre-parênteses' caso ele for antecedido por um número
        if '(' in self.screen.get():
            for k, _ in enumerate(self.screen.get()):
                if len(self.screen.get()) > k + 1:
                    if self.screen.get()[k].isnumeric() and self.screen.get()[k + 1] == '(':
                        self.screen.set(self.screen.get().replace('(', '*('))

        # Adiciona um operador de multiplicação após o 'fecha-parênteses' caso ele for precedido por um número
        if ')' in self.screen.get():
            for k, _ in enumerate(self.screen.get()):
                if len(self.screen.get()) > k + 1:
                    if self.screen.get()[k] == ')' and self.screen.get()[k + 1].isnumeric():
                        self.screen.set(self.screen.get().replace(')', ')*'))

    def math_operation(self):
        """
        Responsável por verficar a operação aritmética a ser realizada
        :return: Seta o resultado das operações aritmética no input
        """
        historic = self.screen.get()
        if self.screen.get() != '' and 'e' not in self.screen.get() and not self.screen.get().isnumeric():

            # Remove os espaços no input
            if ' ' in historic:
                historic = historic.replace(' ', '')
            if ' ' in self.screen.get():
                self.screen.set(self.screen.get().replace(' ', ''))
            if self.valid_operation():
                screen_get_tot = ''
                self.convert_symbols()

                # Verifica se a operação a ser realizada é uma radiciação
                if self.screen.get()[0] == '√':
                    screen_get_tot = self.calculate_square_root()

                # Verifica se a operação a ser realizada é uma fatoração
                elif '!' in self.screen.get():
                    screen_get_tot = self.calculate_factorial(self.screen.get())

                # Verifica se a operação a ser realizada é uma razão centesimal
                elif '%' in self.screen.get():
                    if self.screen.get()[len(self.screen.get()) - 1] == '%':
                        screen_get_tot = self.calculate_percentage(self.screen.get())
                    else:
                        get_first_value = self.calculate_percentage(self.screen.get().split('%')[0])

                        # Verifica se após o % é um número e faz as devidas alterações
                        if self.screen.get().split('%')[1][0].isnumeric():
                            self.screen.set(self.screen.get().replace(self.screen.get().split('%')[1][0],
                                                                      '+' + self.screen.get().split('%')[1]))
                        screen_get_tot = self.basic_operation(str(get_first_value) + (self.screen.get().split('%')[1]))

                # Verifica se a operação a ser realizada é uma operação aritmética básica
                elif self.screen.get()[len(self.screen.get()) - 1].isnumeric() or \
                        self.screen.get()[len(self.screen.get()) - 1] == ')' and '√' not in self.screen.get():
                    if not self.screen.get().isnumeric():
                        if '/' in self.screen.get():
                            if self.screen.get().split('/')[1] == '0' and len(self.screen.get().split('/')[1]) == 1:
                                screen_get_tot = 'Error'
                            else:
                                screen_get_tot = self.basic_operation()
                        else:
                            screen_get_tot = self.basic_operation()

                else:
                    screen_get_tot = 'Error'
            else:
                screen_get_tot = 'Error'

            # verifica o resultado do input e retorna o seu respectivo valor
            if screen_get_tot == 'Error':
                self.screen.set(screen_get_tot)
                self.historic.add_historic(str(historic) + ' = Error')
            else:

                # Formata o resultado em notação cientifica caso seja maior que 15 digitos
                if len(str(screen_get_tot)) > 15:
                    self.screen.set(str(screen_get_tot)[0:15] + 'e')
                    self.control.set(str(screen_get_tot)[0:15] + 'e')
                    self.historic.add_historic(str(historic) + ' = ' + str(screen_get_tot))
                else:
                    self.screen.set(str(screen_get_tot))
                    self.historic.add_historic(str(historic) + ' = ' + str(screen_get_tot))
