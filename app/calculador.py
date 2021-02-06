from math import sqrt


def calcular(screen):
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
