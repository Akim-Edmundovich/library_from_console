import pytest

from app import create_id

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

empty_library = []


@pytest.mark.parametrize('library, res', [
    (full_library, 3),
    (empty_library, 1)])
def test_existing_book_by_id(library, res):
    assert create_id(library) == res
