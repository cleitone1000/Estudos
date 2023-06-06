from utilidadescev import moeda

n = float(input('Digite um valor: '))

print(f'{n} com 40% de aumento: {moeda.aumentar(n)}')
print(f'{n} com 5% de desconto: {moeda.diminuir(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'A metade de {n} é: {moeda.metade(n)}')
