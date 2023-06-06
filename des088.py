# Esse programa sorteia números para jogar na megasena

# Importações
from random import randint
from time import sleep


# Declaracões de variáveis
jogo = list()
jogos = list()
cont = 0
vezes = int(input('Quantos jogos você quer gerar? '))

for i in range(vezes):

    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
            if cont >= 6:
                jogo.sort()
                jogos.append(jogo[:])
                jogo.clear()
                cont = 0
                break

for j in range(vezes):
    print(f'Jogo {j+1}: {jogos[j]}')
    sleep(1)
