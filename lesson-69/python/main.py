u"""Fliper.

Você deve escrever um programa que, dadas as posições das portinhas P e R,
neste flíper da figura, diga por qual dos três caminhos, A, B ou C, a bolinha
vai cair!

    Input:
        A entrada é composta por apenas uma linha contendo dois números P e R,
        indicando as posições das duas portinhas do flíper da figura.

    Output:
        A saída do seu programa deve ser também apenas uma linha, contendo uma
        letra maiúscula que indica o caminho por onde a
        bolinha vai cair: 'A', 'B' ou 'C'.

    Restrictions:
        O número P pode ser 0 ou 1. O número R pode ser 0 ou 1.

    Link: https://neps.academy/lesson/69
"""

P, R = input().split()

P = int(P)
R = int(R)

if P == 0:
    print('C')
elif R == 0:
    print('B')
else:
    print('A')
