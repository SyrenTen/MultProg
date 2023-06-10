import pytest
from task_89 import say_hello, know_figures, even_or_not, days_in_months, year_leap_ordinary, calculator, \
    people_on_money, chess, conversion


def test_say_hello_empty(capsys):
    username = []
    say_hello(username)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'We need to find some users!'


def test_say_hello_admin(capsys):
    username = ['Admin']
    say_hello(username)
    captured = capsys.readouterr()
    assert captured.out.strip() == "['Hello Admin, I hope you`re well']"


def test_say_hello_other(capsys):
    username = ['Dima']
    say_hello(username)
    captured = capsys.readouterr()
    assert captured.out.strip() == "['Hello Dima, thank you for logging in again']"


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
                          (5, 0, '/', 'Division by zero!'),
                          (3, 5, 'mod', 3),
                          (6, 3, 'pow', 216),
                          (10, 11, 'div', 0)])
def test_calculator(a, b, operator, expected):
    result = calculator(a, b, operator)
    assert result == expected


@pytest.mark.parametrize('money, expected',
                         [(20, 'На банкноті з номіналом 20 зображен Іван Франко'),
                          (50, 'На банкноті з номіналом 50 зображен Михайло Грушевський')])
def test_people_on_money(money, expected, capsys):
    people_on_money(money)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize('letter, number, expected',
                         [('a', 1, 'Square is black'),
                          ('d', 5, 'Square is white')])
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
