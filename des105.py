def notas(msg):
    """
    Função recebe e analisa várias notas e retorna um dicionário com a análise.
    :param msg:
    :return: Dicionário com análise de dados.
    """

    nota = list()
    while True:
        n = str(input(msg))
        if n == '999':
            break
        elif n.isnumeric():
            nota.append(float(n))
        else:
            print('\033[31mValor incorreto!\033[m')
    media = sum(nota)/len(nota)
    if media >= 7:
        situacao = 'Aprovado'
    elif media < 5:
        situacao = 'Reprovado'
    else:
        situacao = 'Recuperação'

    dic = {
        'Quantidades de notas': len(nota),
        'Maior nota': max(nota),
        'Menor nota': min(nota),
        'Media nota': media,
        'Situação': situacao
    }
    return dic


# Programa Principal
d = notas('Digite suas notas: ')
for k in d.keys():
    print(f'{k:^20}', end='')
print()
for v in d.values():
    print(f'{v:^20}', end='')
print()
