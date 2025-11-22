from db import create_tables
from library import Library
from models import Book, Member

#Create a main program that demonstrates the functionalities of the library system
#main program
create_tables()
library = Library()

def menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. View All Members")
    print("7. Delete member")
    print("8. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        book_no = input("Enter book number: ")
        book = Book(title, author, book_no)
        library.add_book(book)

    elif choice == "2":
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        member = Member(member_id, name)  # Make sure order matches your Member class
        library.register_member(member)

    elif choice == "3":
        member_id = input("Enter member ID: ")
        book_no = input("Enter book number: ")
        library.borrow_book(member_id, book_no)

    elif choice == "4":
        member_id = input("Enter member ID: ")
        book_no = input("Enter book number: ")
        library.return_book(member_id, book_no)

    elif choice == "5":
        print("\nBooks in Library:")
        books = library.get_all_books()  # ✅ Database method
        if not books:  # ✅ Indented under the elif
            print("No books in library.")
        else:
            for book in books:
                print(book)

    elif choice == "6":
        print("\nMembers:")
        members = library.get_all_members()  # ✅ Database method
        if not members:  # ✅ Indented under the elif
            print("No members registered to library.")
        else:
            for member in members:
                print(member)
    elif choice == "7":
        member_id = input("Enter member ID to delete: ")
        library.delete_member(member_id)            

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

