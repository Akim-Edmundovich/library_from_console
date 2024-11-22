import pytest

from app import check_book_by_id

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


@pytest.mark.parametrize('library, book_id, res', [
    (full_library, 1, True),
    (full_library, 100, False)])
def test_existing_book_by_id(library, book_id, res):
    assert check_book_by_id(library, book_id) == res
