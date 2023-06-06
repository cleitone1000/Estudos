lista = []
dec = 'y'
n = 0
while dec == 'y':
    n = int(input('Digite um número: '))

    if n not in lista:
        lista.append(n)
    else:
        print(f'O número {n} já foi digitado, por isso não foi adicionado a lista.')
    dec = input('Deseja continuar? (y/n): ')
print(sorted(lista))
