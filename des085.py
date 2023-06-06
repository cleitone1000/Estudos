lista = [[], []]
for i in range(7):
    numero = int(input(f'Digite o {i+1}° valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    elif numero % 2 == 1:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'Pares: {lista[0]}')
print(f'Impares: {lista[1]}')
