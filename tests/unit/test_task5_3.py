import pytest
from task5_3 import task5p3


@pytest.mark.parametrize('a, x, expected',
                         [(5, 3, 2.236067977499978),
                          (4, 2, 2.0),
                          (4, 8, 2.0000000000000253)])
def test_task5p1(a, x, expected):
    assert task5p3(a, x) == expected
