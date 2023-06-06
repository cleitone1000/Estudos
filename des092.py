from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['ano_nasc'] = int(input('Ano de nascimento (AAAA): '))
cadastro['idade'] = datetime.now().year - cadastro['ano_nasc']
cadastro['ctps'] = str(input('CTPS(Digite 0 caso não tenha): '))
if cadastro['ctps'] != '0':
    cadastro['ano_contratacao'] = int(input('Ano da contratação (AAAA): '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['ano_aposentadoria'] = cadastro['ano_contratacao'] + 35
    cadastro['idade_aposentadoria'] = cadastro['ano_aposentadoria'] - cadastro['ano_nasc']
for k, v in cadastro.items():
    print(f'{k}: {v}')
