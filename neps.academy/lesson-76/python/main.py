u"""Lâmpadas.

Description
        Você está de volta em seu hotel na Tailândia depois de um dia de
    mergulhos. O seu quarto tem duas lâmpadas. Vamos chamá-las de A e B. No
    hotel há dois interruptores, que chamaremos de I1 e I2. Ao apertar I1, a
    lâmpada A acende se estiver apagada, e apaga se estiver acesa. Se apertar
    I2, cada uma das lâmpadas A e a B troca de estado: se estiver apagada, fica
    acesa e se estiver acesa apaga.

        As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar
    um desafio para você. Ele irá apertar os interruptores em uma certa
    sequência, e gostaria que você respondesse o estado final das lâmpadas A e
    B.

    Input:
            A primeira linha contém um número N que representa quantas vezes
        seu amigo irá apertar algum interruptor. Na linha seguinte seguirão N
        números, que pode ser 1, se o interruptor I1 foi apertado, ou 2, se o
        interruptor I2 foi apertado.

    Output:
            Seu programa deve imprimir dois valores, em linhas separadas. Na
        primeira linha, imprima 1 se a lâmpada A estiver acesa no final das
        operações e 0 caso contrário. Na segunda linha, imprima 1 se a lâmpada
        B estiver acesa no final das operações e 0 caso contrário.

    Restrictions:
            2 <= N <= 10^5.

    Link: https://neps.academy/lesson/76
"""

INTERRUPITOR_DUPLO = 2
APAGADA = False
ACESA = True
ZERO = 0
UM = 1


def le_quantidade_acionamento():
    try:
        return int(input())
    except EOFError as error:
        print(error)


def le_acionamentos():
    try:
        return [int(acionamento) for acionamento in input().split()]
    except EOFError as error:
        print(error)


def inverter_estado_lampada(estado_atual):
    if estado_atual == APAGADA:
        return ACESA
    else:
        return APAGADA


def converter_estado_para_saida_esperada(estado_atual):
    if (estado_atual == ACESA):
        return UM
    else:
        return ZERO


def responder(primeira_lampada, segunda_lampada):
    print(converter_estado_para_saida_esperada(primeira_lampada))
    print(converter_estado_para_saida_esperada(segunda_lampada))


estado_primeira_lampada = APAGADA
estado_segunda_lampada = APAGADA
quantidade_acionamento = le_quantidade_acionamento()
acionamentos = le_acionamentos()

for acionamento_atual in range(quantidade_acionamento):
    estado_primeira_lampada = inverter_estado_lampada(estado_primeira_lampada)
    if acionamentos[acionamento_atual] == INTERRUPITOR_DUPLO:
        estado_segunda_lampada = \
            inverter_estado_lampada(estado_segunda_lampada)


responder(estado_primeira_lampada, estado_segunda_lampada)
