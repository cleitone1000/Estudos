numeros = []
par = []
impar = []
while True:
    numeros.append(int(input(f'Digite um número: ')))
    decisao = str(input(f'Quer continuar? (S/N)'))
    if decisao in 'Nn':
        break
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    elif numeros[i] % 2 == 1:
        impar.append(numeros[i])
print(f'Os números digitados foram:{numeros} ')
print(f'Pares: {par}')
print(f'Impares: {impar}')
