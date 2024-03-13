from models.genre import Genre
from helpers import (
    exit_program,
    list_genres,
    find_genre_by_id,
    create_genre,
    update_genre,
    delete_genre,
    list_books,
    find_book_by_title,
    create_book,
    update_book,
    delete_book,
    list_genre_books
)
genres = Genre.get_all()


def main():
    print('\nwelcome to the Library Manager app!'
          '\nHere, you can manage all Books and Genres available in the store'
          '\nTo navigate the menu below, simply type the number of the desired option')
    main_menu()
    

def main_menu():
    print("\nYou´re currently on the main menu"
          "\nplease select one of the options below start navigating")
    print("\n1. Go to Genres menu")
    print("\n0. Exit the program")
    while True:
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            genres_menu()
        else:
            print("\nInvalid choice")


def genres_menu():
    print("You´re currently on the genre menu")
    print("\n1. See all genres")
    print("2. Add a new genre")
    print("3. Go back to the main menu")
    while True:
        choice = input(">")
        if choice == "1":
            display_genre_menu()
        elif choice == "2":
            create_genre()
            genres_menu()
        elif choice == "3":
            main_menu()


def display_genre_menu():
    list_genres()
    print("\nChoose the number of genre to see its options, or:")
    print("Press 0 to go back to the genre menu")
    print("Press d to delete a genre\n")
    while True:
        user_choice = input(">")
        if user_choice == '0':
            genres_menu()
        elif user_choice == "d":
             delete_genre()
             display_genre_menu()
        elif int(user_choice) in range(len(genres)):
            genre_options(user_choice)
        
def genre_options(user_choice):
    while True:
        genre = find_genre_by_id(user_choice)
        print(f"\nYou`re currently viewing all the options for the {genre.name} genre")
        print("\n0. Go back to genres list")
        print("1. add a book to this genre")
        print("2. See all books of the genre")
        print("3. Update this genre")
        choice = input('>')
        if choice == "1":
            create_book()
        elif choice == "2":
            list_genre_books(user_choice)
        elif choice == "3":
            update_genre()
        elif choice == "0":
            display_genre_menu()


if __name__ == "__main__":
    main()

