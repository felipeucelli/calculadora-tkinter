from math import sqrt, factorial
from .historic import Historic


class Calculador:
    def __init__(self, screen, control):
        self.screen = screen
        self.control = control
        self.historic = Historic()

    def duplicate_analysis(self):
        analysis = True
        for k, v in enumerate(self.screen.get()):
            if not v.isnumeric():
                if len(self.screen.get()) > k + 1:
                    if self.screen.get()[k + 1] == v:
                        analysis = False
        return analysis

    def validate_characters(self):
        if self.duplicate_analysis():
            validate_expression = False
            for k, v in enumerate(self.screen.get()):
                if not v.isnumeric() and self.screen.get()[0] != '√' and \
                        self.screen.get()[len(self.screen.get()) - 1] != '!' or v == '(' or \
                        v == ')':
                    if self.screen.get()[len(self.screen.get()) - 1].isnumeric() or \
                            self.screen.get()[len(self.screen.get()) - 1] == ')' or \
                            self.screen.get()[len(self.screen.get()) - 1] == '%' or \
                            self.screen.get()[len(self.screen.get()) - 1] == '!':
                        if len(self.screen.get()) > k + 1:
                            if self.screen.get()[k + 1].isnumeric() or self.screen.get()[k + 1] == '-' or \
                                    self.screen.get()[k + 1] == '(':
                                validate_expression = True
                            elif v == ')':
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

        if all_ok:
            return True
        else:
            return False

    def valid_operation(self):
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
                if self.validate_characters():
                    return True
                else:
                    return False
            else:
                return False

    def basic_operation(self, entry=''):
        if entry == '':
            return eval(self.screen.get())
        else:
            return eval(entry)

    def calculate_square_root(self):
        if len(self.screen.get()) > 1:
            if self.screen.get().count('√') == 1 and self.screen.get()[1] != '-':
                if not self.screen.get().split('√')[1].isnumeric() and self.screen.get()[1].isnumeric():
                    if '!' in self.screen.get():
                        if self.screen.get()[len(self.screen.get()) - 1] == '!':
                            screen_get_tot = sqrt(float(self.calculate_factorial(
                                self.screen.get().split('√')[1])))
                        else:
                            screen_get_tot = 'Error'
                    elif '%' in self.screen.get():
                        if self.screen.get()[len(self.screen.get()) - 1] == '%':
                            screen_get_tot = sqrt(float(self.calculate_percentage(
                                self.screen.get().split('√')[1])))
                        else:
                            screen_get_tot = 'Error'
                    else:
                        square_root = eval(self.screen.get().split('√')[1])
                        if str(square_root)[0] != '-':
                            screen_get_tot = sqrt(float(square_root))
                        else:
                            screen_get_tot = 'Error'
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
        factorial_ok = True
        if screen[len(screen) - 1] == '!':
            if '.' in screen:
                for v in screen.split('.')[1]:
                    if v != '0' and v != '!':
                        factorial_ok = False
                        break
                    else:
                        factorial_ok = True
            else:
                factorial_ok = True
        else:
            factorial_ok = False
        if factorial_ok:
            fact = eval(screen.split('!')[0])
            return factorial(fact)
        else:
            return 'Error'

    @staticmethod
    def calculate_percentage(screen):
        if not screen.split('%')[0].isnumeric():
            percentage_include = ''
            for v in screen:
                if v.isnumeric() or v == '%' or v == '.':
                    percentage_include += v
                else:
                    percentage_include = ''
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
        if '^' in self.screen.get():
            self.screen.set(self.screen.get().replace('^', '**'))
        if 'x' in self.screen.get():
            self.screen.set(self.screen.get().replace('x', '*'))
        if '(' in self.screen.get():
            for k, _ in enumerate(self.screen.get()):
                if len(self.screen.get()) > k + 1:
                    if self.screen.get()[k].isnumeric() and self.screen.get()[k + 1] == '(':
                        self.screen.set(self.screen.get().replace('(', '*('))
        if ')' in self.screen.get():
            for k, _ in enumerate(self.screen.get()):
                if len(self.screen.get()) > k + 1:
                    if self.screen.get()[k] == ')' and self.screen.get()[k + 1].isnumeric():
                        self.screen.set(self.screen.get().replace(')', ')*'))

    def math_operation(self):
        historic = self.screen.get()
        if self.screen.get() != '' and 'e' not in self.screen.get() and not self.screen.get().isnumeric():
            if ' ' in historic:
                historic = historic.replace(' ', '')
            if ' ' in self.screen.get():
                self.screen.set(self.screen.get().replace(' ', ''))
            if self.valid_operation():
                screen_get_tot = ''
                self.convert_symbols()
                if self.screen.get()[0] == '√':
                    screen_get_tot = self.calculate_square_root()
                elif '!' in self.screen.get():
                    screen_get_tot = self.calculate_factorial(self.screen.get())
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
                elif self.screen.get()[len(self.screen.get()) - 1] == '%':
                    screen_get_tot = self.calculate_percentage(self.screen.get())
                else:
                    screen_get_tot = 'Error'
            else:
                screen_get_tot = 'Error'

            if screen_get_tot == 'Error':
                self.screen.set(screen_get_tot)
                self.historic.add_historic(str(historic) + ' = Error')
            else:
                if len(str(screen_get_tot)) > 15:
                    self.screen.set(str(screen_get_tot)[0:15] + 'e')
                    self.control.set(str(screen_get_tot)[0:15] + 'e')
                    self.historic.add_historic(str(historic) + ' = ' + str(screen_get_tot))
                else:
                    self.screen.set(str(screen_get_tot))
                    self.historic.add_historic(str(historic) + ' = ' + str(screen_get_tot))
