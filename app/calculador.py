from math import sqrt
from .historic import add_historic


def valid_operation(screen_tot):
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
                        if screen_tot[k + 1].isnumeric() or screen_tot[k + 1] == '-':
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
                return True
            else:
                return False


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
            if screen_tot[0] == '√':
                if len(screen_tot) > 1:
                    if '+' in screen_tot or '-' in screen_tot or '*' in screen_tot or '/' in screen_tot \
                            or '**' in screen_tot and screen_tot[1].isnumeric():
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
            elif screen_tot[len(screen_tot) - 1].isnumeric() and '√' not in screen_tot:
                if '+' in screen_tot or '-' in screen_tot or '*' in screen_tot or '/' in screen_tot \
                        or '**' in screen_tot:
                    if '/' in screen_tot:
                        if screen_tot.split('/')[1] == '0' and len(screen_tot.split('/')[1]) == 1:
                            screen_get_tot = 'Error'
                        else:
                            screen_get_tot = eval(screen_tot)
                    else:
                        screen_get_tot = eval(screen_tot)
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
