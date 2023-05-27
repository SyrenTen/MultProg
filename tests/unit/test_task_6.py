import pytest

from task_6 import task_6_p1
from task_6 import task_6_p2

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

# I have no idea how to do tests for another parts ,_,
