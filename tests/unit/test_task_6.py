import pytest

from task_6 import calculate_sum, check_even_or_not, text_output, replace_text, count_word_the, find_percent


# test part 1


@pytest.fixture
def num_file():
    numbers = ['3', '10', '212']
    with open('numbers.txt', 'w') as file:
        file.write('\n'.join(numbers))
    yield 'numbers.txt'


@pytest.fixture
def sum_num_file():
    yield 'sum_numbers.txt'


def test_calculate_sum(num_file, sum_num_file):
    calculate_sum()
    with open(sum_num_file, 'r') as file:
        result = float(file.read().strip())
    expected = sum(map(float, ['3', '10', '212']))
    assert result == expected


# test part 2


@pytest.mark.parametrize('num, expected',
                         [(4, '4 is even number'),
                          (5, '5 is not even number')])
def test_check_even_or_not(num, expected):
    check_even_or_not(num)
    with open('even_or_not_number.txt', 'r') as file:
        contents = file.read().strip()
    assert contents == expected


def test_text_output(capsys):
    text_output()
    captured = capsys.readouterr()
    assert captured.out == ("['Python is good language', 'Python good but this txt was deleted', 'Python "
                            "is smart', 'Python is fast', 'In Python you can do anything']\n")


def test_replace_text(capsys):
    replace_text()
    captured = capsys.readouterr()
    assert captured.out == ('C is good language\n'
                            'C good but this txt was deleted\n'
                            'C is smart\n'
                            'C is fast\n'
                            'In C you can do anything\n')


def test_count_word_the(capsys):
    count_word_the()
    captured = capsys.readouterr()
    assert captured.out == ('In Earle_Wayne.txt word the appears 8236 times\n'
                            'In History_of_the_US.txt word the appears 10622 times\n'
                            'In Lilith.txt word the appears 7370 times\n')


def test_find_percent(capsys):
    find_percent()
    captured = capsys.readouterr()
    assert captured.out == ('Percent of small letters in text is 74.90511378599867%\n'
                            'Percent of capital letters in text is 2.092503148389759%\n')
