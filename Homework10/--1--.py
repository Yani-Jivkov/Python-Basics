book_name = input()
books_cheked = 0

while True:
    serched_book = input()

    if serched_book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {books_cheked} books.')
        break

    if serched_book == book_name:
        print(f'You checked {books_cheked} books and found it.')
        break
    else:
        books_cheked += 1
