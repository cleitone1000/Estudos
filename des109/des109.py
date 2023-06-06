from utilidadescev.moeda import moeda, aumentar, diminuir, dobro, metade

n = float(input('Digite um valor: R$'))

print(f'{moeda(n)} com 40% de aumento: {aumentar(n, formatado=True)}')
print(f'{moeda(n)} com 5% de desconto: {diminuir(n, formatado=True)}')
print(f'O dobro de {moeda(n)} é {dobro(n, True)}')
print(f'A metade de {moeda(n)} é: {metade(n, True)}')
