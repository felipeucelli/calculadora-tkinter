from math import sqrt
from .historic import add_historic


def valid_operation(screen_tot, screen, historic):
    validate_symbols = False
    if screen_tot[0].isnumeric() or screen_tot[0] == '√' or screen_tot[0] == '-':
        for c in screen_tot:
            if not c.isalpha() or c == 'x':
                validate_symbols = True
            else:
                validate_symbols = False
                break
        if validate_symbols and '++' not in screen_tot and '--' not in screen_tot and 'xx' not in screen_tot \
                and '//' not in screen_tot and '√√' not in screen_tot and '..' not in screen_tot \
                and '^^' not in screen_tot:
            validate_expression = False
            for k, v in enumerate(screen_tot):
                if not v.isnumeric() and screen_tot[0] != '√':
                    if screen_tot[len(screen_tot) - 1].isnumeric():
                        if screen_tot[k + 1].isnumeric():
                            validate_expression = True
                        else:
                            validate_expression = False
                            break
                    else:
                        validate_expression = False
                        screen.set('Error')
                        add_historic(historic + ' = Error')
                        break
                else:
                    validate_expression = True
            if validate_expression:
                return True
            else:
                return False


def math_operation(screen):
    historic = screen.get()
    screen_tot = screen.get()
    if ' ' in historic:
        historic = historic.replace(' ', '')
    if ' ' in screen_tot:
        screen_tot = screen_tot.replace(' ', '')

    if valid_operation(screen_tot, screen, historic):
        if '^' in screen_tot:
            screen_tot = screen_tot.replace('^', '**')
        if 'x' in screen_tot:
            screen_tot = screen_tot.replace('x', '*')
        if screen_tot[0] == '√' and screen_tot[1].isnumeric():
            if '+' in screen_tot or '-' in screen_tot or '*' in screen_tot or '/' in screen_tot \
                    or '**' in screen_tot:
                square_root = eval(screen_tot.split('√')[1])
                screen.set(sqrt(int(square_root)))
                add_historic(historic + ' = ' + str(sqrt(int(square_root))))
            else:
                square_root = screen_tot.split('√')[1]
                screen.set(sqrt(int(square_root)))
                add_historic(historic + ' = ' + str(sqrt(int(square_root))))
        elif screen_tot[len(screen_tot) - 1].isnumeric() and '√' not in screen_tot:
            screen.set(eval(screen_tot))
            add_historic(historic + ' = ' + str(eval(screen_tot)))
        else:
            screen.set('Error')
            add_historic(historic + ' = Error')
    else:
        screen.set('Error')
        add_historic(historic + ' = Error')

