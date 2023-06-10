import pytest
from task_5 import find_row_sum


@pytest.mark.parametrize('num, expected',
                         [(1, 0.1),
                          (3, 0.002)])
def test_find_row_sum(num, expected):
    assert find_row_sum(num) == expected
