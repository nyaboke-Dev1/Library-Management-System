# Library class
import json
from book import Book
from member import Member
 
class Library:
    def __init__(self):
        self.members = []
        self.books = []
        
    def find_book(self, book_no):
        for book in self.books:
            if book.book_no == book_no:
                return book
        return None
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def add_book(self, book): 
        if self.find_book(book.book_no):
            print(f"Book with number {book.book_no} already exists in the library")
            return
        self.books.append(book)
        print(f"Book {book.title} added to the library")

    def register_member(self, member):
        if self.find_member(member.member_id):
            print(f"Member with ID {member.member_id} already registered")
            return
        self.members.append(member)
        print(f"Member {member.name} registered to the library")

    def borrow_book(self, member_id, book_no):
        member = self.find_member(member_id)
        book = self.find_book(book_no)

        if not member:
            print("Member not found.")
            return
    
        if not book:
            print("Book not found.")
            return

        if not book.is_available():
            print(f"{book.title} is already borrowed.")
            return

        if not member.can_borrow():
            print(f"{member.name} has reached the borrow limit.")
            return

        # process borrowing
        book.borrow()                # change book status
        member.borrow_book(book)     # add book number to member
    
        print(f"{member.name} borrowed '{book.title}' successfully!")


    def return_book(self, member_id, book_no):
        member = self.find_member(member_id)
        book = self.find_book(book_no)

        if not member:
            print("Member not found.")
            return
    
        if not book:
            print("Book not found.")
            return

        if book_no not in member.borrowed_books:
            print(f"{member.name} did not borrow this book.")
            return

        # process returning
        book.return_book()
        member.return_book(book)
    
        print(f"{member.name} returned '{book.title}' successfully!")


    def __str__(self):
        return f"Library has {len(self.books)} books and {len(self.members)} members."