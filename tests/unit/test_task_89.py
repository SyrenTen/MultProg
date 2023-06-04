import pytest
from task_89 import hello_site
from task_89 import know_figures
from task_89 import even_or_not
from task_89 import days_in_months
from task_89 import year_leap_ordinary
from task_89 import calculator
from task_89 import people_on_money
from task_89 import chess
from task_89 import conversion


def test_hello_site_empty(capsys):
    username = []
    hello_site(username)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'We need to find some users!'


def test_hello_site_admin(capsys):
    username = ['Admin']
    hello_site(username)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello Admin, I hope you`re well'


def test_hello_site_other(capsys):
    username = ['Dima', 'User1234', 'Misha', 'Alex']
    hello_site(username)
    captured = capsys.readouterr()
    assert captured.out.strip() == ('Hello Dima, thank you for logging in again\n'
                                    'Hello User1234, thank you for logging in again\n'
                                    'Hello Misha, thank you for logging in again\n'
                                    'Hello Alex, thank you for logging in again')


@pytest.mark.parametrize('num, expected',
                         [(4, 'Figure with 4 sides is Quadrangle'),
                          (5, 'Figure with 5 sides is Pentagon'),
                          (2, 'Error. Enter number from 3 to 6')])
def test_know_figures(num, expected, capsys):
    know_figures(num)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('number, expected',
                         [(0, '0 is even'),
                          (5, '5 is not even'),
                          (2, '2 is even')])
def test_even_or_not(number, expected, capsys):
    even_or_not(number)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('m_name, expected',
                         [('February', 'Days in February: 28 or 29'),
                          ('March', 'Days in March: 31'),
                          ('lol', 'Error. Wrong month name')])
def test_days_in_months(m_name, expected, capsys):
    days_in_months(m_name)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('n_year, expected',
                         [(2100, 'Ordinary year'),
                          (2000, 'Leap year')])
def test_year_leap_ordinary(n_year, expected, capsys):
    year_leap_ordinary(n_year)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('a, b, operator, expected',
                         [(2, 6, '+', 8),
                          (10, 4, '-', 6),
                          (63, 25, '*', 1575),
                          (10, 0, '*', 0),
                          (15, 6, '/', 2.5),
                          # (5, 0, '/', 'Division by zero!'),
                          (3, 5, 'mod', 3),
                          (6, 3, 'pow', 216),
                          (10, 11, 'div', 0)])
def test_calculator(a, b, operator, expected):
    result = calculator(a, b, operator)
    assert result == expected


# def test_calculator_div_zero(capsys):
#     a = 5
#     b = 0
#     operation = '/'
#     calculator(a, b, operation)
#     captured = capsys.readouterr()
#     assert captured.out.strip() == ''


@pytest.mark.parametrize('money, expected',
                         [(20, 'На банкноті з номіналом 20 зображен Іван Франко'),
                          (50, 'На банкноті з номіналом 50 зображен Михайло Грушевський'),
                          (100, 'На банкноті з номіналом 100 зображен Тарас Шевченко'),
                          (200, 'На банкноті з номіналом 200 зображен Леся Українка'),
                          (500, 'На банкноті з номіналом 500 зображен Григорій Сковорода'),
                          (1000, 'На банкноті з номіналом 1000 зображен Володимир Вернадський')])
def test_people_on_money(money, expected, capsys):
    people_on_money(money)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('letter, number, expected',
                         [('a', 1, 'Square is black'),
                          ('d', 5, 'Square is white'),
                          ('g', 7, 'Square is black'),
                          ('c', 2, 'Square is white')])
def test_chess(letter, number, expected, capsys):
    chess(letter, number)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('choice, number, expected',
                         [(1, 2018, '11111100010'),
                          (2, 11111100010, '2018')])
def test_conversion(choice, number, expected, capsys):
    conversion(choice, number)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
