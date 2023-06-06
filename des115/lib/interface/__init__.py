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


def linha(tam=42):
    print('#'*tam)


def cabeçalho(txt=''):
    linha()
    print(txt.center(42).upper())
    linha()


def menu(lista):
    c = 1
    for item in lista:
        print(f'{c}.{item}')
        c += 1
    linha()
    op = leiaint('Digite sua opção: ')
    return op
