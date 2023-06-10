import pytest
from task_4 import find_sum


@pytest.mark.parametrize('num, expected', [(1, 0.5), (2, 1.25)])
def test_find_sum(num, expected):
    assert find_sum(num) == expected
