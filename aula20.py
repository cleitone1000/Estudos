def titulo(msg):
    print('#'*30)
    print(msg)
    print('#'*30)


# Programa Principal
titulo('Sistemas de Alunos')
titulo('Cadastro de Funcionários')
titulo('Erro do Sistema')


def soma(a, b):
    print(f'a={a}, b={b}')
    s = a + b
    print(f'A soma de {a} e {b} é {s}')



soma(b=4, a=5)


def contador(*n):
    tam = len(n)
    print(f'Recebí os valores {n} e o total de números são {tam}.')


contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)


valores = [2, 4, 6, 8]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1


dobra(valores)
print(valores)