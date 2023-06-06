matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna3 = maiorlinha2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite o número da linha {l} e da coluna {c}: '))
        if matrix[l][c] % 2 == 0:
            somapar += matrix[l][c]
        if c == 2:
            somacoluna3 += matrix[l][c]
        if l == 1:
            if matrix[l][c] > maiorlinha2:
                maiorlinha2 = matrix[l][c]
print('Matrix: ')
for p in range(0, 3):
    print(f'[{matrix[p][0]}], [{matrix[p][1]}], [{matrix[p][2]}]')
print(30*'-')
print(f'A soma de todos os números pares digitados é: {somapar}')
print(f'A soma de todos os números da 3° coluna é: {somacoluna3}')
print(f'O maior número digitado na 2° linha é: {maiorlinha2}')
