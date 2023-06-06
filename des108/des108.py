from utilidadescev import moeda

n = float(input('Digite um valor: '))

print(f'{moeda.moeda(n)} com 40% de aumento: {moeda.moeda(moeda.aumentar(n))}')
print(f'{moeda.moeda(n)} com 5% de desconto: {moeda.moeda(moeda.diminuir(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é: {moeda.moeda(moeda.metade(n))}')
