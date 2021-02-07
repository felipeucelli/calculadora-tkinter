from math import sqrt


def calcular(screen):
    screen_tot = screen.get()
    valid = False
    if '^' in screen_tot:
        screen_tot = screen_tot.replace('^', '**')
    if 'x' in screen_tot:
        screen_tot = screen_tot.replace('x', '*')
    if screen_tot[0].isnumeric() or screen_tot[0] == '√' or screen_tot[0] == '-':
        for c in screen_tot:
            if not c.isalpha():
                valid = True
            else:
                valid = False
                break
        if valid and '++' not in screen_tot and '--' not in screen_tot and 'xx' not in screen_tot \
                and '//' not in screen_tot and '√√' not in screen_tot and '..' not in screen_tot:
            if screen_tot[0] == '√' and screen_tot[1].isnumeric():
                if '+' in screen_tot or '-' in screen_tot or '*' in screen_tot or '/' in screen_tot \
                        or '**' in screen_tot:
                    square_root = eval(screen_tot.split('√')[1])
                    screen.set(sqrt(int(square_root)))
                else:
                    square_root = screen_tot.split('√')[1]
                    screen.set(sqrt(int(square_root)))
            elif screen_tot[len(screen_tot) - 1].isnumeric() and '√' not in screen_tot:
                screen.set(eval(screen_tot))
            else:
                screen.set('Error')
        else:
            screen.set('Error')
    else:
        screen.set('Error')
