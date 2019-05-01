u"""Medalhas OBI 2016 - Segunda Fase - Nível Júnior.

A natação foi um dos esportes mais emocionantes das Olimpíadas do Rio. Houve
até uma prova na qual três atletas chegaram empatados, cada um recebendo uma
medalha de prata! Normalmente, porém, os três primeiros colocados terminam a
prova em tempos distintos e, portanto, temos a distribuição mais comum de
medalhas: o nadador que terminou no menor tempo recebe medalha de ouro; o
nadador que terminou com o segundo menor tempo recebe medalha de prata; e o que
terminou com o terceiro menor tempo recebe medalha de bronze. Neste problema,
dados os três tempos distintos de finalização da prova, dos três nadadores que
ganharam medalhas, seu programa deve dizer quem ganhou medalha de ouro, quem
ganhou prata e quem ganhou bronze.

    Entrada
        A primeira linha da entrada contém um inteiro T1, indicando o tempo em
        que o nadador 1 terminou a prova. A segunda linha da entrada contém um
        inteiro T2, indicando o tempo de finalização do nadador 2. Por fim, a
        terceira linha da entrada contém um inteiro T3, indicando o tempo em
        que o nadador 3 terminou a prova.

    Saída
        Seu programa deve imprimir três linhas na saída. A primeira linha deve
        conter o número do nadador que ganhou medalha de ouro; a segunda linha,
        o número do nadador que ganhou prata; e a terceira linha, o número do
        nadador que levou bronze.

    Restrições
        Os tempos T1, T2 e T3 são inteiros distintos,
        com valores entre 1 e 1000, inclusive.

    Link: https://neps.academy/problem/2
"""

QNT_TOTAL_TEMPO = 3
ZERO = 0

"""Lista de objetos do tipo atleta"""
atletas = [{"tempo": int(input()), "nadador": i+1} for i in range(
    ZERO, QNT_TOTAL_TEMPO)]

for x in range(0, 3):
    for i in range(1, len(atletas)):
        if atletas[i]['tempo'] < atletas[i-1]['tempo']:
            temp = atletas[i-1]
            atletas[i-1] = atletas[i]
            atletas[i] = temp

for atleta in atletas:
    print(atleta['nadador'])
