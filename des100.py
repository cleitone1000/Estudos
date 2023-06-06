from random import randint

numeros = ['', '', '', '', '']
soma = 0


def sorteia(num):
    print(f'Os números sorteados foram: ', end='')
    for i in range(len(num)):
        num[i] = randint(0, 10)
        print(f'{num[i]} ', end='')
    print()


def somapar(num, som):
    print('Os números somados foram: ', end='')
    for i in range(len(num)):
        if num[i] % 2 == 0:
            som += num[i]
            print(f'{num[i]} ', end='')
    print(f' = {som}')


sorteia(numeros)
somapar(numeros, soma)
