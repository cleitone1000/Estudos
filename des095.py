gols = list()
galera = list()
cont = 'N'
jogador = dict()
while True:
    jogador.clear()
    total = 0
    nome = str(input('Nome do Jogador: '))
    qtd_partidas = int(input(f'Quantas partidas o jogador {nome} jogou: '))
    for i in range(qtd_partidas):
        gols.append(int(input(f'Quantos gols na partida {i}: ')))
    for c in range(len(gols)):
        total += gols[c]
    jogador = {
        'nome': nome,
        'gols': gols[:],
        'total': total
    }
    galera.append(jogador.copy())
    gols.clear()
    while True:
        cont = str(input('Deseja continuar?(S/N) ').upper()[0])
        if cont in 'SN':
            break
        if cont not in 'SN':
            print('Resposta inválida, digite Sim ou Não(S/N): ')
    if cont == 'N':
        break

print('#'*30)
print('Código   ', end='')
for e in jogador.keys():
    print(f'{e:<15}', end='')
print()
for k, v in enumerate(galera):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print()

print('#'*60)

while True:
    busca = int(input('Digite o código do jogador ou 999 para parar: '))
    if busca == 999:
        break
    if busca >= len(galera):
        print(f'O código digitado não está no cadastro, digite um número igual ou menor que {len(galera)}: ')
    else:
        print(f'Levantamento do jogador {galera[busca]["nome"]}')
        for i, g in enumerate(galera[busca]['gols']):
            print(f'Na partida {i} ele fez {g} gols.')
        print(f'Total de gols: {galera[busca]["total"]}')
