from copy import deepcopy

import pytest

from app import update_book

before_edit_library = [
    {
        "id": 1,
        "title": "1",
        "author": "1",
        "year": 1,
        "status": "в наличии"
    }
]

after_edit_library = [
    {
        "id": 1,
        "title": "1",
        "author": "1",
        "year": 1,
        "status": "выдана"
    }
]


@pytest.mark.parametrize('library, book_id, status, result',
                         [
                             (deepcopy(before_edit_library), 1, 'выдана',
                              after_edit_library),
                             (deepcopy(before_edit_library), 1,
                              'НЕКОРРЕКТНЫЙ СТАТУС', before_edit_library),
                         ])
def test_change_status_book(library, book_id, status, result):
    assert update_book(library, book_id, status) == result
