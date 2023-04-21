#Multi-paradigm programming language: Task 5.2, Maslova Vitaliia, idk
import math
print('Multi-paradigm programming language: Task 5.2')

print('Maslova Vitaliia, idk')

n = int(input('Input n: '))
c = 0

if n == 0:
    c = 1
else:
    while n != 0:
        c += 1
        n //= 10

print('c =', c)

