import pytest
from task5_2 import numbers_amount


@pytest.mark.parametrize('num, expected',
                         [(1234, 4),
                          (0, 1)])
def test_numbers_amount(num, expected):
    assert numbers_amount(num) == expected
