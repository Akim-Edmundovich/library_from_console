from app import delete_book

before_deleting_library = [
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

after_deleting_library = [
    {
        "id": 2,
        "title": "2",
        "author": "2",
        "year": 2,
        "status": "в наличии"
    }
]


def test_delete_existing_book():
    assert delete_book(before_deleting_library, 1) == after_deleting_library


def test_delete_nonexistent_book():
    assert delete_book(before_deleting_library, 3) != after_deleting_library
