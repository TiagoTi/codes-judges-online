"""Title.

Description

    Input:
        Input detail.

    Output:
        output detail.

    Restrictions:
        restrictions details.

    Link:
"""

VOGAIS = ['a', 'e', 'i', 'o', 'u']


def eh_vogal(letra):
    return letra in VOGAIS


def buscar_risadas():
    try:
        return input()
    except EOFError as error:
        print(error)
        return None


def filtrar_consoantes(risada):
    return ''.join(list(filter(eh_vogal, risada)))


def tem_sequencia(risada):
    if len(risada) == 1:
        return True
    for i in VOGAIS:
        contador = 0
        for j in risada:
            if i == j:
                contador += 1
                if contador > 1:
                    return True
            else:
                contador = 0
        return False


def resposta(tem_sequencia):
    if tem_sequencia is True:
        return 'S'
    if tem_sequencia is False:
        return 'N'
    else:
        return None


print(resposta(tem_sequencia(filtrar_consoantes(buscar_risadas()))))
