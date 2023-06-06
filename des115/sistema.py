from des115.lib.interface import *
from time import sleep
from des115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

arquivo = open('cadastro.txt', 'a')

# Programa Principal
while True:
    cabeçalho('Menu Principal')
    resposta = menu(['Visualizar', 'Cadastrar', 'Sair'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar nome e idade
        cabeçalho('Novo Cadastro')
        cadastrar(arq)
        linha()
    elif resposta == 3:
        print('Muito Obrigado!')
        linha()
        break
    else:
        print('\033[31mOpção incorreta!\033[m')
        linha()
        sleep(2)
# Comentário para simular mudança
