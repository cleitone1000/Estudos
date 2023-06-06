matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = float(input(f'Digite o número da linha {l} e da coluna {c}: '))

print('Matrix: ')
for p in range(0,3):
        print(f'[{matrix[p][0]}], [{matrix[p][1]}], [{matrix[p][2]}]')
