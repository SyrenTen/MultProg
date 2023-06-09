import pytest
from task_11 import find_orientation
from unittest.mock import patch, mock_open


@pytest.mark.parametrize('content, expected', [
    ('Its a positive article', 'Positive'),
    ('Its is a negative article', 'Negative'),
    ('Its is a neutral article', 'Neutral')
])
def test_find_orientation(content, expected, capsys):
    with patch('builtins.open', mock_open(read_data=content)):
        article_name = 'test_article_orientation.txt'
        find_orientation(article_name)

    captured = capsys.readouterr()
    assert captured.out.strip() == f'Article orientation: {expected}'
