# Multi-paradigm programming language: Task 5.3, Maslova Vitaliia, idk
from utils import validation

print('''Multi-paradigm programming language: Task 5.3')
Maslova Vitaliia, idk''')


def task5p3(a, x):
    if a < 0:
        print('Error: a not positive')
        exit()

    e = 1e-4

    while True:
        sqr = (1 / 2) * (x + (a / x))
        if abs(sqr - x) < e:
            break
        x = sqr

    return sqr


if __name__ == '__main__':
    inp_a = validation('positive num', float)
    inp_x = validation('x', float)
    sqrt = task5p3(inp_a, inp_x)
    print('Sqrt of', inp_a, 'is', sqrt)
