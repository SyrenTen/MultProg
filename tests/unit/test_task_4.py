import pytest
from task_4 import find_sum


@pytest.mark.parametrize('num, expected', [(1, 0.5), (2, 1.25)])
def test_task_4(num, expected):
    assert find_sum(num) == expected
