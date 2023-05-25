# Multi-paradigm programming language: Task 5.2, Maslova Vitaliia, idk
from utils import validation

print('''Multi-paradigm programming language: Task 5.2
Maslova Vitaliia, idk''')


def task5p2(num):
    count = 0

    if num == 0:
        count = 1
    else:
        while num != 0:
            count += 1
            num //= 10

    return count


if __name__ == '__main__':
    n = validation('num', int)
    inp_count = task5p2(n)
    print('count =', inp_count)
