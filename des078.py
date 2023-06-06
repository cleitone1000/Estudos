#lista = [int(input(' Digite um valor numérico: ')), int(input('Digite um valor numérico: ')),int(input('Digite um valor númérico: ')),int(input('Digite um valor númérico: ')),int(input('Digite um valor númérico: '))]
lista = []
for i in range(5):
    lista.append(int(input(f'Digite o {i+1}° valor numérico: ')))
print(f'O maior número digitado é o {max(lista)}, e o menor número digitado é o {min(lista)}')
print(lista)
