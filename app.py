#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p

from Listdatabase import *

USER_CHOICE = """
Enter:
- 'a' to add a new book
_ 'l' to list all books
_ 'r' to mark a book as read
_ 'd' to delete a book
- 'q' to quit

Your choice:"""

def menu():
    user_input = input(USER_CHOICEaa)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            promt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknow commad. Please try again.")

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    add_book(name, author)

menu()
