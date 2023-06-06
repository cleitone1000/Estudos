cont = 0
expressao = str(input('Digite uma expressão: '))
for i in range(len(expressao)):
    if expressao[i] == '(':
        cont += 1
    elif expressao[i] == ')':
        cont -=1
if cont == 0:
    print(f'A expressão {expressao} está correta.')
else:
    print(f'A espressão {expressao} está incorreta.')
    if cont > 0:
        print('Há um ou mais parênteses abertos.')
    else:
        print('Há um ou mais parênteses fechados a mais.')
