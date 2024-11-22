from app import book_list

full_library = [
    {
        "id": 1,
        "title": "1",
        "author": "1",
        "year": 1,
        "status": "в наличии"
    }
]


def test_book_list():
    assert book_list(full_library) == full_library


def test_empty_book_list():
    assert book_list([]) == 'Библиотека пуста.'
