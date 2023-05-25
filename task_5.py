# Multi-paradigm programming language: Task 5.1, Maslova Vitaliia, idk
import math
from utils import validation

print('''Multi-paradigm programming language: Task 5.1'
Maslova Vitaliia, idk''')


def task5p1(num):
    e = 1e-4
    a = 1
    amount = 0
    while a > e:
        a = 10 ** (-num) * math.factorial(num - 1)
        amount += a
        num += 1

    return amount


if __name__ == '__main__':
    n = validation('num', int)
    am = task5p1(n)
    print('Sum =', am)
