def area(l, c):
    tamanho = l * c
    print(f'A área do terreno de largura {l} e comprimento {c} é {tamanho} m²')


def titulo(msg):
    print('#'*30)
    print(msg)
    print('#'*30)


titulo('Cálculo de Terreno')

largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))
area(largura, comprimento)
