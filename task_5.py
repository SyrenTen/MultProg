# Multi-paradigm programming language: Task 5.1, Maslova Vitaliia, idk
import math as m
from utils import validate_input

print('''Multi-paradigm programming language: Task 5.1'
Maslova Vitaliia, idk''')


def find_row_sum(number):
    E = 10 - 4
    a = 10 ** (-number) * m.factorial(number - 1)
    count = a

    while a > E:
        a = 10 ** (-number) * m.factorial(number - 1)
        count += a
        number += 1

    return count


if __name__ == '__main__':
    num = validate_input('number', int)
    amount = find_row_sum(num)
    print(f'Sum = {amount}')
