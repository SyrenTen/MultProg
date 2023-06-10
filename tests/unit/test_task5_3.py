import pytest
from task5_3 import square_root


@pytest.mark.parametrize('a, x, expected',
                         [(5, 3, 2.236067977499978),
                          (4, 2, 2.0)])
def test_task5p1(a, x, expected):
    assert square_root(a, x) == expected
