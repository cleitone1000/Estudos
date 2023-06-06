def voto(anonasc):
    """
    Função para calcular se você precisa votar nas eleições
    :param anonasc: Ano nascimento
    :return: Negado = menor de 16 anos
            Opcional = entre 16 e 18 anos e maior de 70 anos
            Obrigatório = maior de 70 anos

    criado por @cleitone1000
    """
    from datetime import date
    idade = date.today().year - anonasc
    if idade < 16:
        return 'Negado'
    elif 16 <= idade < 18 or idade > 70:
        return 'Opcional'
    else:
        return 'Obrigatório'


print(voto(int(input('Digite o seu ano de nascimento: '))))
