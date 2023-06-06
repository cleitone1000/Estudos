def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print(f'\033[0;31mValor incorreto!\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaint('Digite um valor numérico: ')
print(f'\033[34m {n} \033[m')
