import random

from utils import validate_input


def say_hello(username):
    if not username:
        print('We need to find some users!')
    else:
        greet = ['Hello Admin, I hope you`re well' if user == 'Admin' else f'Hello {user}, thank you for ' \
                                                                           f'logging in again' for user in username]
        print(greet)


def know_figures(number):
    FIGURE = {3: 'Triangle',
              4: 'Quadrangle',
              5: 'Pentagon',
              6: 'Hexagon'}

    print('Error. Enter number from 3 to 6') if number not in FIGURE else print(f'Figure with {number} sides '
                                                                                f'is {FIGURE[number]}')
    # if number in FIGURE dont work for some reason
    # code works correctly with condition number not in FIGURE


def num_ending():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        num_out = str(i)
        if i == 1:
            num_out += 'st'
        elif i == 2:
            num_out += 'nd'
        elif i == 3:
            num_out += 'rd'
        else:
            num_out += 'th'

        print(num_out)


def even_or_not(numb):
    print(f'{numb} is even') if numb % 2 == 0 else print(f'{numb} is not even')


def days_in_months(month_name):
    MONTHS = {'January': 31, 'February': '28 or 29', 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
              'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

    print(f'Days in {month_name}: {MONTHS[month_name]}') if month_name in MONTHS else print('Error. Wrong month name')


def year_leap_ordinary(year_num):
    print('Leap year') if year_num % 4 == 0 and (year_num % 100 != 0 or year_num % 400 == 0) else print('Ordinary year')


def num_sum_bef_zero():
    digit_sum = 0
    while True:
        digit = validate_input('number for task 7', int)
        if digit == 0:
            break
        digit_sum += digit

    print(f'Sum of numbers: {digit_sum}')


def calculator(in_a, in_b, operation):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else 'Division by zero!',
        'mod': lambda a, b: a % b,
        'pow': lambda a, b: a ** b,
        'div': lambda a, b: a // b if b != 0 else 'Division by zero!'
    }
    return operations.get(operation, 'Wrong operator')(in_a, in_b)


def people_on_money(money):
    people = {20: 'Іван Франко',
              50: 'Михайло Грушевський',
              100: 'Тарас Шевченко',
              200: 'Леся Українка',
              500: 'Григорій Сковорода',
              1000: 'Володимир Вернадський'}
    print(f'На банкноті з номіналом {money} '
          f'зображен {people[money]}') if money in people else print('Немає банкноти з таким номіналом')


def chess(position1, position2):
    letter_list = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    print(f'Square is black') if (letter_list[position1] + position2) % 2 == 0 else print('Square is white')


def conversion(choice, dem_or_bin):
    calc_ten = ''
    # little experiment with case
    match choice:
        case 1:
            while dem_or_bin != 0:
                r = dem_or_bin % 2
                calc_ten = str(r) + calc_ten
                dem_or_bin = dem_or_bin // 2
            print(calc_ten)

        case 2:
            print(sum(int(i) * pow(2, len(str(dem_or_bin)) - j) for j, i in enumerate(str(dem_or_bin), 1)))


def rps(user_choice):
    variants = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(variants)
    if user_choice not in variants:
        print('Error. No such choice')
        exit()

    if user_choice == comp_choice:
        print(f'Computer choice: {comp_choice} - It`s a draw')
    elif ((user_choice == 'rock' and comp_choice == 'scissors') or
          (user_choice == 'paper' and comp_choice == 'rock') or
          (user_choice == 'scissors' and comp_choice == 'paper')):
        print(f'Computer choice: {comp_choice} - You win')
    else:
        print(f'Computer choice: {comp_choice} - Computer win')


if __name__ == '__main__':
    uname = ['Admin', 'Dima', 'User1234', 'Misha', 'Alex']
    say_hello(uname)

    know_figures(validate_input('number from 3 to 6', int))

    num_ending()

    ev_or_nope = validate_input('number', int)
    even_or_not(ev_or_nope)

    months_names = validate_input('month name', str)
    days_in_months(months_names)

    year = validate_input('year', int)
    year_leap_ordinary(year)

    num_sum_bef_zero()

    input_a = validate_input('a', int)
    input_b = validate_input('b', int)
    input_operation = validate_input('operation', str)
    result = calculator(input_a, input_b, input_operation)
    print(result)

    nominal = validate_input('nominal', int)
    people_on_money(nominal)

    pos1 = validate_input('letter from a to h', str)
    pos2 = validate_input('number from 1 to 8', int)
    chess(pos1, pos2)

    print('What conversion you want? Ten to bin or bin to ten?')
    select = validate_input('1 or 2', int)
    inp_ten = validate_input('number', int)
    conversion(select, inp_ten)

    print('Now Rock-Paper-Scissors game!')
    player = validate_input('your choice', str).lower()
    rps(player)
