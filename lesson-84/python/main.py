u"""Soma dos Elementos.

Description
    Nesse problema você receberá um conjunto de valores e sua tarefa é imprimir
    a soma desses valores.

    Input:
        A entrada consiste em duas linhas. A primeira linha possui apenas um
        valor N, representando a quantidade de valores que você deve ler.
        A segunda linha possui N números inteiros separados por um espaço em
        branco.

    Output:
        Você deve imprimir a soma dos N números inteiros lidos na entrada.

    Restrictions:
        1 ≤ N ≤ 100.

    Link: https://neps.academy/lesson/84
"""

from functools import reduce

int(input())
print(reduce((lambda x, y: x + y), [int(i) for i in (input().split())]))
