import pytest
from task_4 import task4


@pytest.mark.parametrize('num, expected', [(1, 0.5), (2, 1.25), (5, 3.8583333333333334)])
def test_task_4(num, expected):
    assert task4(num) == expected
