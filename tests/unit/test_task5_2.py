import pytest
from task5_2 import task5p2


@pytest.mark.parametrize('num, expected',
                         [(1234, 4),
                          (123456, 6),
                          (0, 1)])
def test_task5p1(num, expected):
    assert task5p2(num) == expected
