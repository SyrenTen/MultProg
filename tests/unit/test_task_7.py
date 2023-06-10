import pytest
from task_7 import Point, Line


@pytest.fixture
def dots():
    dot1 = Point(1, 2)
    dot2 = Point(4, 6)
    return Line(dot1, dot2)


def test_find_length(dots):
    assert dots.length() == 5


def test_find_midpoint(dots):
    mid = dots.midpoint()
    assert mid.x == 2.5
    assert mid.y == 4


def test_find_x_projection(dots):
    assert dots.x_projection() == 3


def test_find_y_projection(dots):
    assert dots.y_projection() == 4
