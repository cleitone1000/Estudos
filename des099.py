import time
from time import sleep


def maior(*num):
    cont = mai = 0
    print('Analisando os valores passados...')
    time.sleep(0.5)
    for valor in num:
        print(f'{valor}', end=' ')
        time.sleep(0.5)
        if cont == 0:
            mai = valor
        elif valor > mai:
            mai = valor

        cont += 1
    print(f'\nForam digitados {cont} números e o maior deles é {mai}.')
    time.sleep(0.5)

# Programa principal
maior(3, 4, 5, 6)
maior(5, 4, 6, 3, 7, 2)
