gols = list()
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
print('#'*30)
print(jogador)
print('#'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('#'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p in range(0, len(jogador['gols'])):
    print(f'Na partida {p} ele fez {gols[p]} gols')
print(f'Foi um total de {jogador["total"]}'
      f' gols.')
