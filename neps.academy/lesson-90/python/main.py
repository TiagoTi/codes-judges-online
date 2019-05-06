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




def buscar_risadas():
    try:
        return input()
    except EOFError as error:
        print(error)
        return None

def _verificar_se_tem_sequencia(texto):
    tem_sequencia = False
    texto = str(filter(lambda x: x in VOGAIS, texto))
    print(texto)
    for vogal in VOGAIS:
        contador = 0
        for letra in texto:
            if vogal == letra:
                print('Tem',vogal,letra, vogal == letra, contador)
                contador += 1
            else:
                print('NTem',vogal,letra, vogal == letra, contador)
                contador = 0

            if contador > 1:
                tem_sequencia = True
                break
    return tem_sequencia



def validar_se_eh_uma_risada(risada):
    if len(risada) == 1 and risada in VOGAIS:
        return True

    if _verificar_se_tem_sequencia(risada):
        return True
    return None


def responder_problema(resposta):
    if resposta is True:
        return "S"
    if resposta is False:
        return "N"
    else:
        raise Exception('Tipo invalido')

VOGAIS = ['a', 'e', 'i', 'o', 'u']
risada = buscar_risadas()
resposta = validar_se_eh_uma_risada(risada)
try:
    responder_problema(resposta)
except Exception as error:
    print(error)