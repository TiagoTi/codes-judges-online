u"""Prêmio do Milhão.

    Alice e Bia criaram uma página na Internet com informações sobre o
Macaco-prego-de-peito-amarelo, uma espécie em extinção. A página mostra como
todos podem ajudar a manter o habitat natural para evitar que a espécie
seja extinta.
    Uma empresa gostou tanto da iniciativa de Alice e Bia que prometeu doar um
prêmio para que as duas amigas possam realizar outras iniciativas semelhantes.
A empresa decidiu que o prêmio seria dado quando a soma do número de acessos à
página chegasse a 1 milhão.
    Dada a lista de acessos diários que ocorreram à página de Alice e Bia,
escreva um programa para determinar quantos dias foram necessários para a soma
dos acessos chegar a 1 milhão e as amigas ganharem o prêmio.

    Input:
        A primeira linha da entrada contém um número inteiro N, que indica o
        número de dias que a lista contém. Cada uma das linhas seguintes contém
        um único inteiro A, o número de acessos em um dia. O primeiro número
        dado indica o número de acessos no primeiro dia, o segundo número dado
        indica o número de acessos no segundo dia, e assim por diante.

    Output:
        Seu programa deve escrever na saída uma única linha, contendo um único
        número inteiro, o número de dias que foram necessários para a soma dos
        acessos à pagina de Alice e Bia chegar a 1000000..

    Restrictions:
        1≤N≤10^3, ou seja, a lista tem no máximo 1000 números
        0≤A≤10^6, ou seja, cada inteiro A da lista é positivo e menor do que ou
        igual a 1 milhão.
        A soma de todos os valores A da lista é maior do que ou igual a 1
        milhão (ou seja, Alice e Bia certamente ganham o prêmio).

    Link:
"""


def load_inputs():
    """Load a list of input listed on the especification."""
    try:
        numbers_of_days = int(input())
        list_of_acces_per_day = []

        for _ in range(numbers_of_days):
            list_of_acces_per_day.append(int(input()))

        return {
            'target_access': 1000000,
            'numbers_of_days': numbers_of_days,
            'list_of_acces_per_day': list_of_acces_per_day
        }
    except EOFError as error:
        print(error)


def processing(data):
    """Count how many day use to get x access."""
    days = 0
    account = 0
    index = 0

    while account < data['target_access']:
        account += data['list_of_acces_per_day'][index]
        days += 1
        index += 1

    return days


def output_solution(days):
    """Print on output standout the soluction."""
    print(days)


def main():
    """Run all soluction togheter."""
    output_solution(processing(load_inputs()))


if __name__ == '__main__':
    main()
