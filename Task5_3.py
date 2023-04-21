#Multi-paradigm programming language: Task 5.3, Maslova Vitaliia, idk
import math
print('Multi-paradigm programming language: Task 5.3')

print('Maslova Vitaliia, idk')

a = float(input('Input positive num: '))
if a < 0:
    print('Error: a not positive')
    exit()

x = float(input('Input x: '))
e = 1e-4

while True:
    sqr = (1/2)*(x+(a/x))
    if abs(sqr-x) < e:
        break
    x = sqr

print('Sqrt of', a, 'is', sqr)


