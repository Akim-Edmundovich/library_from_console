import pytest
from copy import deepcopy
from unittest.mock import patch

from app import create_book

before_creating_library = [
    {
        "id": 1,
        "title": "1",
        "author": "1",
        "year": 1,
        "status": "в наличии"
    }
]

new_book_outside_library = {
    "id": 2,
    "title": "2",
    "author": "2",
    "year": 2,
    "status": "в наличии"
}

result_library = [
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


@pytest.mark.parametrize(
    'mock_inputs, before_library, new_book', [
        (["2", "2", "2"],
         deepcopy(before_creating_library),
         new_book_outside_library),
    ]
)
def test_create_book(mock_inputs, before_library, new_book):
    with patch('builtins.input', side_effect=mock_inputs):
        result = create_book(before_library)
        print(result)
        assert result == new_book
