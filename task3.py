# Multi-paradigm programming language: Task 3, Maslova Vitaliia, idk

import math as m
from utils import validate_input

print('''Multi-paradigm programming language: Task 3'
Maslova Vitaliia, idk''')


def validate_number():
    num = validate_input('x', float)
    degree = validate_input('alfa', float)
    return num, degree


while True:
    x, alfa = validate_number()

    if x < 2:
        print('Error: x too small')
    elif not m.sin(alfa):
        print('Error: cant divide by zero -.-')
    else:
        y = m.log(x**3 - 8) + 1 / m.sin(alfa)
        print(f'y = {y}')
        break
