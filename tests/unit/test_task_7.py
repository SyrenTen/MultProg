import pytest
from task_7 import Point
from task_7 import Line


def test_task_7_length():
    dot1 = Point(1, 2)
    dot2 = Point(4, 6)
    line = Line(dot1, dot2)
    assert line.length() == 5


def test_task_7_midpoint():
    dot1 = Point(1, 2)
    dot2 = Point(4, 6)
    line = Line(dot1, dot2)
    mid = line.midpoint()
    assert mid.x == 2.5
    assert mid.y == 4


def test_task7_x_projection():
    dot1 = Point(1, 2)
    dot2 = Point(4, 6)
    line = Line(dot1, dot2)
    assert line.x_projection() == 3


def test_task7_y_projection():
    dot1 = Point(1, 2)
    dot2 = Point(4, 6)
    line = Line(dot1, dot2)
    assert line.y_projection() == 4
