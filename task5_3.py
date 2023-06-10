# Multi-paradigm programming language: Task 5.3, Maslova Vitaliia, idk
from utils import validate_input

print('''Multi-paradigm programming language: Task 5.3')
Maslova Vitaliia, idk''')


def square_root(a, x):
    if a < 0:
        print('Error: a not positive')
        return None

    E = 1e-4

    while True:
        sqr = (1 / 2) * (x + (a / x))
        if abs(sqr - x) < E:
            break
        x = sqr

    return sqr


if __name__ == '__main__':
    inp_a = validate_input('positive number', float)
    inp_x = validate_input('x', float)
    sqrt = square_root(inp_a, inp_x)
    print(f'Sqrt of {inp_a} is {sqrt}')
