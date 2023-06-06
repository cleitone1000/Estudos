import time
from random import randint
from operator import itemgetter
ranking =()
jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}

print('#'*30)
for k, v in jogadores.items():
    print(f'{k} jogou {v}')
    time.sleep(1)
print('#'*30)
print('#'*10, f'RANKING:', '#'*10)
print('#'*30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#ranking = sorted(jogadores.items, key=itemgetter(1), reverse=True)
for i in range(len(ranking)):
    print(f'{i+1}°{ranking[i][0]:10}: {ranking[i][1]:10}')
    time.sleep(1)
