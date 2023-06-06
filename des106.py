from random import randint

while True:
    estilo = randint(0, 7)
    texto = randint(30, 37)
    back = randint(40, 47)
    # cor = str(f'\033[{estilo};{texto};{back}m')
    h = str(input('\033[1;33;41mInteractive Help: \033[m'))
    if h.upper() == 'FIM':
        print('Fim!')
        break
    print(f'\033[{estilo};{texto};{back}m {help(h)}\033[m')
