# Interactive Help
# help(print())
# print(input.__doc__)


# docstring
def contador(i, f, p):
    """
    Contador
    :param i: Início do contador
    :param f: Fim do contador
    :param p: Passo(intervalo) de contagem
    :return: nenhum
    """
    c = i
    while c <= f:
        print(f'{c}', end='-')
        c += p
    print('Fim!')


# contador(1, 100, 20)
# print(contador.__doc__)


# Argumentos opcionais
def somar(a=0, b=0, c=0):
    """
    Função soma 3 valores opcionais e imprime o valor final
    :param a: primeiro argumento opcional
    :param b: segundo argumento opcional
    :param c: terceira opção
    :return: nenhum
    Função criada por @cleitone1000
    """
    s = a+b+c
    print(f'A soma vale {s}')


#somar(2)


# Escopo de variáveis



# Retorno de resultados
