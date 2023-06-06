from utilidadescev.moeda import moeda


def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg).replace(',', '.').strip())
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \033[0;31m{entrada} é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)
