def fatorial(fat, show=False):
    """
    Calcula o fatorial
    :param fat: O número que será calculado o fatorial
    :param show: mostra o cálculo
    :return: nenhum
    """
    fa = cont = fat
    for c in range(fat-1, 1, -1):
        fat *= c
    if not show:
        print(fat)
    else:
        print(f'{fa}! = ', end='')
        for c in range(cont, 1, -1):
            print(f'{c} x ', end='')
        print(f'1 = {fat}')


fatorial(4, False)
