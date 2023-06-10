# Multi-paradigm programming language: Task 4, Maslova Vitaliia, idk
from utils import validate_input

print('''Multi-paradigm programming language: Task 4
Maslova Vitaliia, idk''')


def find_sum(number):
    count = 0

    for i in range(1, number + 1):
        term = (2 * i - 1) / (2 * i)
        count += term

    return count


if __name__ == '__main__':
    num = validate_input('number', int)
    amount = find_sum(num)
    print(f'Sum = {amount}')
