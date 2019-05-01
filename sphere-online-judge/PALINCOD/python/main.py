"""PALINCOD - Palindrome or not.

Description
        A palindrome is a word, phrase, number, or other sequence of units that
    can be read the same way in either direction, with general allowances for
    adjustments to punctuatiom and word dividers for eg.,
    HELLOLLEH is a Palindrome string,
    and
    123456789 is not a Palindrome number.

    Input:
        t - number of testcases [ t < 1000 ].
        On each of the next t lines given string.

    Output:
        For each next t lines output the dataset number as a decimal integer
        (start counting at one), a space and "YES" if the given input is
        palindrome, or "NO" if the input is not.

    Restrictions:
        restrictions details.

    Link:
"""

HALF = 2

# Input
try:
    number_of_testcase = int(input())
    string_cases = []
    for _ in range(number_of_testcase):
        string_cases.append(input())
except EOFError as error:
    print(error)

for case in string_cases:
    half_length_of_string = int(len(case)/HALF)
    is_palindrome = "\"YES\""
    for i in range(half_length_of_string):
        if not (case[i] == case[len(case)-1-i]):
            is_palindrome = "\"NO\""
            break
    print(string_cases.index(case) +1, is_palindrome)
