# Multi-paradigm programming language: Task 4, Maslova Vitaliia, idk
from utils import validation

print('''Multi-paradigm programming language: Task 4
Maslova Vitaliia, idk''')


def task4(num):
    amount = 0

    for i in range(1, num + 1):
        term = (2 * i - 1) / (2 * i)
        amount += term

    return amount


if __name__ == '__main__':
    n = validation('num', int)
    am = task4(n)
    print('Sum = ', am)
