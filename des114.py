import requests


def verificar_site(site):
    try:
        response = requests.get(site)
        if response.status_code == 200:
            print(f'O site {site} está acessível.')
        else:
            print(f'O site {site} está inacessível, código de status {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro ao acessar o site {e}')


# Programa Principal
link = str(input('Digite um site para ser verificado: '))
verificar_site(link)
