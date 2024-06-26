# lib/helpers.py
from models.genre import Genre
from models.book import Book

def exit_program():
    print("\nThank you for using the Library Manager app, see you soon!")
    exit()


def list_genres():
    genres = Genre.get_all()
    print('\nThese are all the genres available at the moment:')
    for i, genre in enumerate(genres, start=1):
         print(i, genre.name)


def find_genre_by_name():
    name = input("\nEnter the genre's name: ")
    genre = Genre.find_by_name(name)
    print(genre) if genre else print(
        f'\ngenre {name} not found')
    

def find_genre_by_id(n):
    genre = Genre.find_by_id(n)
    return genre
    
    
    
def create_genre():
    name = input("\nEnter the genre's name: ")
    try:
        genre = Genre.create(name)
        print(f'\nSuccess, {genre.name} was added to the collection\n')
    except Exception as exc:
        print("\nError creating genre: ", exc)


def update_genre(genre):
    id_ = genre.id
    if genre := Genre.find_by_id(id_):
        try:
            name = input("\nEnter the genre's new name: ")
            genre.name = name
            genre.update()
            print(f'\nSuccess! genre name updated to {genre.name}')
        except Exception as exc:
            print("\nError updating genre: ", exc)
    else:
        print(f'\ngenre {id_} not found')


def delete_genre(n):
    id_ = int(n)
    genre = Genre.find_by_id(id_)
    books = genre.books()
    for book in books:
            print(f'{book.title} deleted')
            book.delete()
    if genre:= Genre.find_by_id(n):
            print(f'{genre.name} deleted')
            genre.delete()
    else:
        print('Please, type the number of one of the existing genres above to be deleted')


def list_books():
    books = Book.get_all()
    index = 1
    for book in books:
        print(f'{ index}.Title: {book.title}, Author: {book.author}')
        index += 1


def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(f'\n{book}') if book else print(
        f'\nbook {title} not found')


def create_book(genre):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    genre_id = genre.id
    try:
        book = Book.create(title, author, genre_id)
        print(f'Success! Book {book.title} was added to the collection')
    except Exception as exc:
        print("Error creating book: ", exc)


def update_book(n):
    id_ = n
    if book := Book.find_by_id(id_):
        id = book.genre_id
        try:
            title = input("Enter the books's new title: ")
            book.title = title
            author = input("Enter the book's new Author:")
            book.author = author
            genre_id = id
            book.genre_id = genre_id
            book.update()
            print(f'\nSuccess, Book´s title and author were updated to Title: {book.title} and Author: {book.author}\n')
        except Exception as exc:
            print("Error updating book: ", exc)
    else:
        print(f'book {id_} not found')


def delete_book(n):
    id_ = n
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'\nbook {book.title} deleted')
    else:
        print(f'book {id_} not found')


def list_genre_books(genre):
        print(f'\nThese are all the books belonging to the {genre.name} genre:\n')
        if len(genre.books()) == 0:
            print('No books belonging to this genre are available at the moment')
        else:
            books = genre.books()
            for i, book in enumerate(books, start=1):
                print(i, f"Title: {book.title}, Author: {book.author}, {genre.name}")