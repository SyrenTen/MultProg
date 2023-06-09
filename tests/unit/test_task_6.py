import pytest

from task_6 import task_6_p1
from task_6 import task_6_p2, task_6_p3, task_6_p4, task_6_p6, task_6_p8, task_6_p9


# test part 1


@pytest.fixture
def num_file():
    numbers = ['3', '10', '212']
    with open('numbers.txt', 'w') as f:
        f.write('\n'.join(numbers))
    yield 'numbers.txt'


@pytest.fixture
def sum_num_file():
    yield 'sum_numbers.txt'


def test_task_6_p1(num_file, sum_num_file):
    task_6_p1()
    with open(sum_num_file, 'r') as f:
        result = float(f.read().strip())
    expected = sum(map(float, ['3', '10', '212']))
    assert result == expected


# test part 2


@pytest.mark.parametrize('num, expected',
                         [(4, '4 is even number'),
                          (5, '5 is not even number')])
def test_task_6_p2(num, expected):
    task_6_p2(num)
    with open('even_number.txt', 'r') as file:
        contents = file.read().strip()
    assert contents == expected


def test_task_6_p3(capsys):
    task_6_p3()
    captured = capsys.readouterr()
    assert captured.out == ("['Python is good language', 'Python good but this txt was deleted', 'Python "
                            "is smart', 'Python is fast', 'In Python you can do anything']\n")


def test_task_6_p4(capsys):
    task_6_p4()
    captured = capsys.readouterr()
    assert captured.out == ('C is good language\n'
                            'C good but this txt was deleted\n'
                            'C is smart\n'
                            'C is fast\n'
                            'In C you can do anything\n')


def test_task_6_p6(capsys):
    task_6_p6()
    captured = capsys.readouterr()
    assert captured.out == ('In Earle_Wayne.txt word the appears 8236 times\n'
                            'In History_of_the_US.txt word the appears 10622 times\n'
                            'In Lilith.txt word the appears 7370 times\n')


# def test_task_6_p8(capsys):
#     with open('chapters.txt', 'r', encoding='utf-8') as chapters_file:
#         chapters_content = chapters_file.read()
#     expected = "CHAPTER I. START IN LIFECHAPTER II. SLAVERY AND ESCAPECHAPTER III." \
#                "WRECKED ON A DESERT ISLANDCHAPTER IV." \
#                "FIRST WEEKS ON THE ISLANDCHAPTER V. BUILDS A HOUSE—THE JOURNALCHAPTER VI. " \
#                "ILL AND CONSCIENCE-STRICKENCHAPTER VII. AGRICULTURAL EXPERIENCECHAPTER VIII. " \
#                "SURVEYS HIS POSITIONCHAPTER IX. A BOATCHAPTER X. TAMES GOATSCHAPTER XI. " \
#                "FINDS PRINT OF MAN’S FOOT ON THE SANDCHAPTER XII. A CAVE RETREATCHAPTER XIII. " \
#                "WRECK OF A SPANISH SHIPCHAPTER XIV. A DREAM REALISEDCHAPTER XV. " \
#                "FRIDAY’S EDUCATIONCHAPTER XVI. RESCUE OF PRISONERS FROM CANNIBALSCHAPTER XVII. " \
#                "VISIT OF MUTINEERSCHAPTER XVIII." \
#                "THE SHIP RECOVEREDCHAPTER XIX. RETURN TO ENGLANDCHAPTER XX. FIGHT BETWEEN FRIDAY AND A BEAR"
#     assert chapters_content == expected

def test_task_6_p9(capsys):
    task_6_p9()
    captured = capsys.readouterr()
    assert captured.out == ('Percent of small letters in text is 74.90511378599867%\n'
                            'Percent of capital letters in text is 2.092503148389759%\n')
