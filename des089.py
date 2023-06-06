cad = list()
dados = list()
continuar = ''
while True:
    cad.append(str(input('Aluno: ')))
    cad.append(float(input('Nota 1: ')))
    cad.append(float(input('Nota 2: ')))
    dados.append(cad[:])
    cad.clear()
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar == 'N' or continuar == 'n':
        break

for i in range(len(dados)):
    print(f'-='*30)
    print(f'{"Número":<4}{"Nome":<10}{"Média":>8}')
    print('-'*26)
    print(f'{i:<4} {dados[i][0]:10}     {dados[i][1]}     {dados[i][2]}')

while True:
    aluno = int(input('De qual aluno você quer ver as notas? Digite 999 para sair: '))
    if aluno == 999:
        break
    print(f'{dados[aluno][0]}    {dados[aluno][1]}    {dados[aluno][2]}')
