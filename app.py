import json


def create_book(library) -> dict:
    """
    Создает книгу. Возвращает словарь с данными о книге.
    """
    try:

        title = input('Введите название книги: ')
        while not title:
            title = input('Название не может быть пустым: ')

        author = input('Введите автора книги: ')
        while not author:
            author = input('У книги должен быть автор: ')

        while True:
            year = input('Укажите год написания книги (целое число): ')

            try:
                year = int(year)
                if year != 0:
                    break

                else:
                    print('Введите целое число!')

            except ValueError:
                print('Введите целое число!')

    except Exception as e:
        print('ERROR" ', e)

    new_book_id = create_id(library)

    new_book = {
        'id': new_book_id,
        'title': title,
        'author': author,
        'year': year,
        'status': 'в наличии'
    }

    return new_book


def delete_book(library: list, book_id: int):
    """Удаляет книгу по ID"""
    book_id = validate_input_id(book_id)

    for book in library:
        if book['id'] == book_id:
            library.pop(library.index(book))
            print(f'\nКнига {book["title"]} удалена из библиотеки.')
            return library


def get_book(library: list, title=None, author=None, year=None):
    """
    Фильтр по названию, автору или году.
    Выводит список книг, с которыми совпали введенные параметры.
    """
    books_filter = []

    title = input('Название (Enter - пропустить): ')
    author = input('Автор (Enter - пропустить): ')

    year = input('Год (Enter - пропустить): ')

    for book in library:
        if (book['title'] == title or
                book['author'] == author or
                str(book['year']) == year):
            books_filter.append(book)

    return f'\nРезультаты поиска: \n{books_filter}' \
        if books_filter else '\nКниги не найдены'


def update_book(library: list, book_id: int, status='в наличии'):
    """Редактирует статус книги"""
    tags = ['в наличии', 'выдана']
    """Редактирует статус книги"""
    book_id = validate_input_id(book_id)

    if status in tags:
        book_to_edit = [book for book in library if book['id'] == book_id]
        book_to_edit[0]['status'] = status
        print(f'Статус "{book_to_edit[0]["title"]}" изменен на {status}')
        return library

    else:
        print('\n! --- Введен неверный статус --- !')
        return library


def book_list(library):
    """Выводит список всех книг (если они имеются)"""
    return library if library else '\n! --- Библиотека пуста --- !'


def validate_input_id(book_id):
    """
    Валидирует введенное значение ID.
    """
    if book_id:
        try:
            book_id = int(book_id)

        except ValueError:
            return False
    else:
        print('! --- ID не может быть пустым --- !')
        return False

    return int(book_id)


def check_book_by_id(library, book_id):
    book_id = validate_input_id(book_id)
    if library:
        for book in library:
            if book['id'] == book_id:
                return True
            else:
                print('\n! --- Книги с таким ID не существует --- !')
                return False


def create_id(library: list):
    """Создает id на основе имеющихся в библиотеке"""

    return max(book['id'] for book in library) + 1 if library else 1


def get_or_create_json_file(filename='library.json'):
    """
    Извлекает данные из файла библиотеки.
    Если файла нет - создает его.
    Если файл есть и содержит некорректные данные -
    очищает его и создает там пустой список.
    """

    try:
        with open(filename, 'r+', encoding='utf-8') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError("Файл должен содержать список")

            except (json.JSONDecodeError, ValueError):
                file.seek(0)
                file.truncate()
                data = []
                json.dump(data, file, ensure_ascii=False, indent=4)
            return data

    except FileNotFoundError:
        with open(filename, 'r+', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        return []


def save_to_json(data, file='library.json'):
    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def main():
    """
    Управление программой.
    """
    hello = input('''
           --- Главное меню --- 
           Введите команду:
           1 - добавить книгу
           2 - обзор книги
           3 - редактировать книгу
           4 - удалить книгу
           5 - список книг
           6 - главное меню
           000 - выход \n''')

    library = get_or_create_json_file('library.json')

    command_list = ['1', '2', '3', '4', '5', '6', '000']

    if hello not in command_list:
        print('! --- Несуществующая команда --- !')

    else:
        while hello != '000':

            # Создать книгу
            if hello == '1':
                new_book = create_book(library)
                print(new_book)
                library.append(new_book)
                save_to_json(library)
                print('\nКнига добавлена')
                main()

            # Обзор книги
            elif hello == '2':
                if library:
                    print(get_book(library))
                    main()
                else:
                    print('\n! --- Библиотека пуста --- !')
                    main()

            # Редактирование книги
            elif hello == '3':
                if library:
                    book_id = input('Введите ID книги для редактирования: ')

                    if check_book_by_id(library, book_id):
                        status = input(
                            'Выберите статус: "в наличии", "выдана": ')
                        library = update_book(library, book_id, status)
                        save_to_json(library)
                        main()
                    else:
                        main()
                else:
                    print('\n! --- Библиотека пуста --- !')
                    main()

            # Удалить книгу
            elif hello == '4':
                if library:
                    book_id = input('Введите ID книги для удаления: ')

                    if check_book_by_id(library, book_id):
                        books = delete_book(library, book_id)
                        save_to_json(books)
                        main()
                    else:
                        main()
                else:
                    print('\n! --- Библиотека пуста --- !')
                    main()

            # Список всех книг
            elif hello == '5':
                if library:
                    print(book_list(library))
                    main()
                else:
                    print('\n! --- Библиотека пуста --- !')
                    main()
            # Главное меню
            elif hello == '6':
                main()


if __name__ == '__main__':
    main()
