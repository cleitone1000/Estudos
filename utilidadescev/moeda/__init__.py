def aumentar(valor=0, taxa=40, formatado=False):
    """
    Função recebe um parâmetro e devolve com um aumento de 40%
    valor: números inteiros e decimais
    :return: retorna o valor com o aumento de 40 por cento
    """
    res = valor + valor * (taxa/100)
    return res if formatado is False else moeda(res)


def diminuir(valor=0, taxa=5, formatado=False):
    """
    Função para diminuir 5%
    :valor: valor monetário
    :taxa: valor opcional para operação.
    :return: Valor com a diminuição da taxa
    """
    res = valor - valor * (taxa / 100)
    return res if formatado is False else moeda(res)


def dobro(valor=0, formatado=False):
    """
    Função para dobrar valor
    :param valor: valores decimais
    :param formatado: Parâmetro opcional para retornar o valor como moeda
    :return: retorna o dobro do valor passado
    """
    res = valor * 2
    return res if formatado is False else moeda(res)


def metade(valor=0, formatado=False):
    """
    Função para obter metade do valor passado
    :param valor: números inteiros e decimais
    :param formatado: Parâmetro opcional para retornar o valor formatado como moeda
    :return: retorna a metade do valor passado
    """
    res = valor / 2
    return res if formatado is False else moeda(res)


def moeda(valor=0.0, moeda='R$'):
    """
    Função para formatar o valor presentado
    :param valor: Valor a ser formatado
    :param moeda: Informar a moeda que será usada, se não informar o padrão é real
    :return: string com valor monetário formatado
    """
    # m = str(input(f'A moeda atual é {moeda}, você quer alterar?: S/N'))
    msg = str(f'{moeda}{valor:.2f}'.replace('.', ','))
    return msg


def resumo(n=0, taxaa=40, taxar=5):
    """
    Função que resume as outras funções
    :param n: valor processado
    :param taxaa: taxa de aumento
    :param taxar: taxa de redução
    :return: Retorna um resumo de operações feitas com o valor passado
    """
    print('#'*40)
    print(f'Resumo:'.center(40))
    print('#'*40)
    print(f'{moeda(n)} com {taxaa}% de aumento: {aumentar(n, taxaa, True)}')
    print(f'{moeda(n)} com {taxar}% de desconto: {diminuir(n, taxar, True)}')
    print(f'O dobro de {moeda(n)} é {dobro(n, True)}')
    print(f'A metade de {moeda(n)} é: {metade(n, True)}')
    print('#'*40)
