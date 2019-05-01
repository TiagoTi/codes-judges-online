u"""Aprovado ou Reprovado.

Description:
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
        correspondem as duas notas que o aluno conquistou esse semestre.

    Output:
        A saída do seu programa deve ser apenas uma linha. Caso o aluno tenha
        sido aprovado informe "Aprovado", caso o aluno tenha sido reprovado
        informe "Reprovado" e caso ele esteja de recuperação
        informe "Recuperacao".

    Restrictions:
        None.

    Link: https://neps.academy/lesson/70
"""

# Input
try:
    A, B = input().split()
    A = float(A)
    B = float(B)
except EOFError as error:
    print(error)


R = (A + B) / 2.0

if R >= 7:
    S = 'Aprovado'
elif R >= 4:
    S = 'Recuperacao'
else:
    S = 'Reprovado'

# Output
print(S)
