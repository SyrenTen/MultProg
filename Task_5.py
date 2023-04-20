#Multi-paradigm programming language: Task 5.1, Maslova Vitaliia, idk
import math
print('Multi-paradigm programming language: Task 5.1')

print('Maslova Vitaliia, idk')

e = 1e-4
n = int(input('Input n:'))
a = 1
sum = 0

while a > e:
    a = 10**(-n)*math.factorial(n-1)
    sum += a

print("sum = ", sum)
