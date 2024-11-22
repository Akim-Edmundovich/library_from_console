import pytest
from unittest.mock import patch
from app import get_book

full_library = [
    {
        "id": 1,
        "title": "1",
        "author": "1",
        "year": 1,
        "status": "в наличии"
    },
    {
        "id": 2,
        "title": "2",
        "author": "2",
        "year": 2,
        "status": "в наличии"
    }
]

filter_library = [
    {
        "id": 1,
        "title": "1",
        "author": "1",
        "year": 1,
        "status": "в наличии"
    }
]


@pytest.mark.parametrize('mock_inputs, result', [
    (["1", "", ""], filter_library),
    (["", "1", ""], filter_library),
    (["", "", '1'], filter_library),
    (["", "", ""], []),
])
def test_find_book(mock_inputs, result):
    with patch('builtins.input', side_effect=mock_inputs):
        assert get_book(full_library) == f'\nРезультаты поиска: \n{result}' \
            if result else '\nКниги не найдены'
