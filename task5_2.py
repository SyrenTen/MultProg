# Multi-paradigm programming language: Task 5.2, Maslova Vitaliia, idk
from utils import validate_input

print('''Multi-paradigm programming language: Task 5.2
Maslova Vitaliia, idk''')


def numbers_amount(number):
    count = 0
    if not number:
        return 1
    while number:
        count += 1
        number //= 10
    return count


if __name__ == '__main__':
    num = validate_input('number', int)
    inp_count = numbers_amount(num)
    print(f'Count = {inp_count}')
