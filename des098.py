import time
from time import sleep


def contador(inicio, fim, passo):
    # Conta de 1 a 10 incrementando 1
    print('Primeira Sequência:')
    for i in range(10):
        print(i, end='', flush=True)
        time.sleep(0.5)
    print()
    # Conta de 10 a 1 decrementando 2
    print('Segunda sequência: ')
    for j in range(10, 1, -2):
        print(j, end='', flush=True)
        time.sleep(0.5)
    print()
    # Contador usa os parâmetros passados
    print('Terceira Sequência')
    if passo < 0:
        if inicio < fim:
            passo *= -1
            print(f'Passo assumiu o valor {passo}.')
        elif inicio == fim:
            passo = 0
            print(f'Passo assumiu o valor {passo}.')
    elif passo == 0:
        if inicio < fim:
            passo = 1
            print(f'Passo assumiu o valor {passo}.')
        elif inicio > fim:
            passo = -1
            print(f'Passo asumiu o valor {passo}.')
    elif passo > 0:
        if inicio == fim:
            passo = 0
            print(f'Passo assumiu o valor {passo}.')
        elif inicio > fim:
            passo *= -1
            print(f'Passo assumiu o valor {passo}.')

    for k in range(inicio, fim, passo):
        print(k, end='', flush=True)
        time.sleep(0.5)
    print()


# Programa Principal
ini = int(input('Início: '))
fi = int(input('Fim: '))
pa = int(input('Passo: '))

contador(ini, fi, pa)
