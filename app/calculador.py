from math import sqrt, factorial
from .historic import add_historic


def validate_characters(screen_tot):
    if '++' not in screen_tot and '--' not in screen_tot and 'xx' not in screen_tot \
            and '//' not in screen_tot and '√√' not in screen_tot and '..' not in screen_tot \
            and '^^' not in screen_tot and '!!' not in screen_tot and '%%' not in screen_tot:
        validate_expression = False
        for k, v in enumerate(screen_tot):
            if not v.isnumeric() and screen_tot[0] != '√' and screen_tot[len(screen_tot) - 1] != '!' or v == '(' or \
                    v == ')':
                if screen_tot[len(screen_tot) - 1].isnumeric() or screen_tot[len(screen_tot) - 1] == ')' or \
                        screen_tot[len(screen_tot) - 1] == '%' or screen_tot[len(screen_tot) - 1] == '!':
                    if len(screen_tot) > k + 1:
                        if screen_tot[k + 1].isnumeric() or screen_tot[k + 1] == '-' or screen_tot[k + 1] == '(':
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
            if '(' in screen_tot or ')' in screen_tot:
                if screen_tot.count('(') == screen_tot.count(')'):
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


def valid_operation(screen_tot):
    validate_symbols = False
    if screen_tot[0].isnumeric() or screen_tot[0] == '√' or screen_tot[0] == '-' or screen_tot[0] == '(':
        for c in screen_tot:
            if not c.isalpha() or c == 'x':
                validate_symbols = True
            else:
                validate_symbols = False
                break
        if validate_symbols:
            if validate_characters(screen_tot):
                return True
            else:
                return False
        else:
            return False


def calculate_factorial(screen_tot):
    factorial_ok = True
    if '.' in screen_tot:
        for v in screen_tot.split('.')[1]:
            if v != '0' and v != '!':
                factorial_ok = False
                break
            else:
                factorial_ok = True
    else:
        factorial_ok = True
    if factorial_ok:
        fact = eval(screen_tot.split('!')[0])
        return factorial(fact)
    else:
        return 'Error'


def calculate_percentage(screen_tot):
    percentage_include = ''
    for k, v in enumerate(screen_tot):
        if v.isnumeric() or v == '%':
            percentage_include += v
        else:
            percentage_include = ''
    percentage_include = percentage_include.split('%')[0]
    first_value = screen_tot.split(percentage_include + '%')[0]
    percentage_conversion = float(percentage_include) / 100
    convert_first_value = first_value.replace(first_value[len(first_value) - 1], '')
    percentage_tot = float(convert_first_value) * float(percentage_conversion)
    return eval(first_value + str(percentage_tot))


def math_operation(screen):
    historic = screen.get()
    screen_tot = screen.get()
    if screen_tot != '' and 'e' not in screen_tot:
        if ' ' in historic:
            historic = historic.replace(' ', '')
        if ' ' in screen_tot:
            screen_tot = screen_tot.replace(' ', '')
        if valid_operation(screen_tot):
            screen_get_tot = ''
            if '^' in screen_tot:
                screen_tot = screen_tot.replace('^', '**')
            if 'x' in screen_tot:
                screen_tot = screen_tot.replace('x', '*')
            if '(' in screen_tot:
                for k, v in enumerate(screen_tot):
                    if len(screen_tot) > k + 1:
                        if screen_tot[k].isnumeric() and screen_tot[k + 1] == '(':
                            screen_tot = screen_tot.replace('(', '*(')
            if ')' in screen_tot:
                for k, v in enumerate(screen_tot):
                    if len(screen_tot) > k + 1:
                        if screen_tot[k] == ')' and screen_tot[k + 1].isnumeric() and \
                                screen_tot[len(screen_tot) - 1] != ')':
                            screen_tot = screen_tot.replace(')', ')*')
            if screen_tot[0] == '√':
                if len(screen_tot) > 1:
                    if '+' in screen_tot or '-' in screen_tot or '*' in screen_tot or '/' in screen_tot \
                            or '**' in screen_tot or '!' in screen_tot and screen_tot[1].isnumeric():
                        if '!' in screen_tot:
                            if screen_tot[len(screen_tot) - 1] == '!':
                                screen_get_tot = sqrt(float(calculate_factorial(screen_tot.split('√')[1])))
                            else:
                                screen_get_tot = 'Error'
                        else:
                            square_root = eval(screen_tot.split('√')[1])
                            if str(square_root)[0] != '-':
                                screen_get_tot = sqrt(float(square_root))
                            else:
                                screen_get_tot = 'Error'
                    else:
                        square_root = screen_tot.split('√')[1]
                        screen_get_tot = sqrt(float(square_root))
                else:
                    screen_get_tot = 'Error'
            elif screen_tot[len(screen_tot) - 1] == '!':
                screen_get_tot = calculate_factorial(screen_tot)
            elif screen_tot[len(screen_tot) - 1].isnumeric() and '√' not in screen_tot or \
                    screen_tot[len(screen_tot) - 1] == ')':
                if '+' in screen_tot or '-' in screen_tot or '*' in screen_tot or '/' in screen_tot \
                        or '**' in screen_tot:
                    if '/' in screen_tot:
                        if screen_tot.split('/')[1] == '0' and len(screen_tot.split('/')[1]) == 1:
                            screen_get_tot = 'Error'
                        else:
                            screen_get_tot = eval(screen_tot)
                    else:
                        screen_get_tot = eval(screen_tot)
            elif screen_tot[len(screen_tot) - 1] == '%':
                screen_get_tot = calculate_percentage(screen_tot)
            else:
                screen_get_tot = 'Error'
        else:
            screen_get_tot = 'Error'

        if screen_get_tot == 'Error':
            screen.set(screen_get_tot)
            add_historic(str(historic) + ' = Error')
        else:
            if len(str(screen_get_tot)) > 15:
                screen.set(str(screen_get_tot)[:15] + 'e')
                add_historic(str(historic) + ' = ' + str(screen_get_tot))
            else:
                screen.set(str(screen_get_tot))
                add_historic(str(historic) + ' = ' + str(screen_get_tot))
