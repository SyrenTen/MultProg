import pytest
from task_11 import find_orientation


@pytest.mark.parametrize('article_name, expected',
                         [('test_task_11_positive.txt', 'Article orientation: Positive'),
                          ('test_task_11_neutral.txt', 'Article orientation: Neutral'),
                          ('test_task_11_negative.txt', 'Article orientation: Negative')])
def test_find_orientation(article_name, expected, capsys):
    find_orientation(article_name)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
