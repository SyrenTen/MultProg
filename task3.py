# Multi-paradigm programming language: Task 3, Maslova Vitaliia, idk

import math
from utils import validation

print('''Multi-paradigm programming language: Task 3'
Maslova Vitaliia, idk''')

while True:
    x = validation('x', float)
    alfa = validation('alfa', float)

    if x < 2:
        print('Error: x too small')
    elif math.sin(alfa) == 0:
        print('Error: cant divide by zero -.-')
    else:
        y = math.log(x**3 - 8) + 1 / math.sin(alfa)
        print(f'y = {y}')
        break
