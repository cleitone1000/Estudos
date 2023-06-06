def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg).replace(',', '.').strip())
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print(f'\033[0;31mValor incorreto!\033[m')
        if ok:
            break
    return valor


# Programa principal
try:
    n = leiaint('Digite um valor numérico: ')
    print(f'\033[34m {n} \033[m')
except ValueError:
    print('errou:')
else:
    print('thai tome thai thai tome tome')
