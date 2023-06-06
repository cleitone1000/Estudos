cadastro = list()
pessoa = dict()
soma_idade = media_idade = 0
print('#'*30)
print('        Cadastro        ')
print('#'*30)
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo(M/F): ').upper()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('Sexo inválido! Digite M ou F: ')
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    cadastro.append(pessoa.copy())
    parar = str(input('Quer continuar(S/N): '))
    if parar in 'Nn':
        break
print('#'*30)
print(f'A. Ao todo temos {len(cadastro)} pessoas cadastradas.')
media_idade = soma_idade/len(cadastro)
print(f'B. A média de idade é de {media_idade:5.2f} anos.')
print('C. As mulheres cadastradas são: ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print('')
print('D. Pessoas que estão com a idade acima da média: ', end='')
for i in cadastro:
    if i['idade'] > media_idade:
        print(i['nome'], end='')
print('')
