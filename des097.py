while True:
    def escreva(lst):
        print('#' * len(lst))
        print(lst)
        print('#'*len(lst))


    # Programa Principal
    msg = str(input('Digite uma mensagem:(999 para parar) '))
    # Decisão para saída do programa
    if msg == '999':
        break

    escreva(msg)
