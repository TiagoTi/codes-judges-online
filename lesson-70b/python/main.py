u"""Aprovado ou Reprovado.

Description
    No Colégio Neps Academy (CNA) um aluno é aprovado por média se ele obtiver
    uma média final maior ou igual a 7, caso o aluno tenha uma média menor que
    7 mas maior ou igual a 4 ele está de recuperação, caso ele tenha uma média
    menor que 4 o aluno está reprovado.

    A média é calculada com a nota das duas provas aplicadas no semestre e
    corresponde simplesmente a média aritimética das duas notas.

    Baseado nas duas notas do aluno, indique o resultado final do aluno:
    "Aprovado", "Reprovado" ou "Recuperacao".

    Input:
        A entrada consiste de apenas uma linha com as notas A e B, que
        correspondem as duas notas que o aluno conquistou esse semestre.detail.

    Output:
        output detail.

    Restrictions:
        A saída do seu programa deve ser apenas uma linha. Caso o aluno tenha
        sido aprovado informe "Aprovado", caso o aluno tenha sido reprovado
        informe "Reprovado" e caso ele esteja de recuperação
        informe "Recuperacao"..

    Link: https://neps.academy/lesson/70
"""

u"""Input.
Uma linha com os dois valores
"""

try:
    A, B = [float(x) for x in input().split()]
except EOFError as error:
    print(error)

S = (A + B) / 2.0

if S >= 7.0:
    print('Aprovado')
elif S >= 4.0 and S < 7:
    print('Recuperacao')
else:
    print('Reprovado')

