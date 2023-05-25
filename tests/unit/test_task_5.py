import pytest
from task_5 import task5p1


@pytest.mark.parametrize('num, expected',
                         [(1, 0.11303200000000001),
                          (3, 0.003032),
                          (5, 0.00043200000000000004)])
def test_task5p1(num, expected):
    assert task5p1(num) == expected
