from des115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'O arquivo {nome} foi criado com sucesso.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar(arquivo):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'Erro ao abrir arquivo {arquivo}.')
    else:
        try:
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            a.write(f'{nome};{idade}\n')
        except:
            print(f'Erro ao cadastrar.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

