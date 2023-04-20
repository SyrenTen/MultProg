#Multi-paradigm programming language: Task 3, Maslova Vitaliia, idk

import math

print('Multi-paradigm programming language: Task 3')

print('Maslova Vitaliia, idk')

x = float(input('Input x: '))
alfa = float(input('Input alfa: '))

if x < 2:
    print('Error: x too small')
elif math.sin(alfa) == 0:
    print('Error: cant divide by zero -.-')
else:
    y = math.log(x**3 - 8) + 1/math.sin(alfa)
    print("y = ", y)
