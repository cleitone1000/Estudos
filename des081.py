flag = 'y'
lista = []
cont = i = 0
while flag == 'y':
    n = int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    flag = str(input('Quer continuar?(y/n): '))
print(f'foram digitados {len(lista)} números.')
print(f'Lista: {sorted(lista , reverse=True)}')
if 5 not in lista:
    print('O número 5 não está na lista.')
else:
    for pos in range(len(lista)):
        if lista[pos] == 5:
            i += 1
    print(f'O número 5 está na lista {i} vezes.')
