#book class
class Book:
    def __init__(self, title, author, book_no, status="available"):
        self.title = title
        self.author = author
        self.book_no = book_no
        self.status = status
            
    def borrow(self):
        print(f"You have borrowed {self.title} by {self.author}")
    def return_book(self):
        print(f"You have returned {self.title} by {self.author}")
    def book_status(self):
        print(f"Status of {self.title}: {self.status}")
    def __str__(self):
        return(f"Book Title: {self.title}, Author: {self.author}, Book No: {self.book_no}")
        
        
#member class
class Member:
    def __init__(self, name, member_id, borrowed_books = []):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
    
    def borrow_book(self, book): 
        print(f"you have borrowed {book.title} by {book.author}")        
    def return_book(self, book): 
        print(f"you have returned {book.title} by {book.author}")  
    def borrowed_books_list(self):
        return [book.title for book in self.borrowed_books]
        
    def __str__(self):
        return f"Member Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {self.borrowed_books_list()}"         


# Library class
class Library:
    def __init__(self, books, members):
        self.members = members
        self.books = books

    def add_book(self, book): 
        self.books.append(book)
        print(f"Book {book.title} added to the library")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} registered to the library")

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

    def borrow_book(self, member_id, book_no): 
        member = self.find_member(member_id)
        book = self.find_book(book_no)
        if member and book:
            member.borrow_book(book)
        else:
            print("Member or Book not found")

    def return_book(self, member_id, book_no):    
        member = self.find_member(member_id)
        book = self.find_book(book_no)
        if member and book:
            member.return_book(book)
        else:
            print("Member or Book not found")

    def __str__(self):
        return f"Library has {len(self.books)} books and {len(self.members)} members."
    
#Create a main program that demonstrates the functionalities of the library system.
# Add several books and members to the library.
# Perform various operations such as borrowing and returning books.
# Print the state of the library, books, and members at different stages.

#main program
#book structure (title, author, book_no):
book1 = Book("1984", "George Owell", 1)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 2)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 3)

#member structure (name, member_id):
member1 = Member("Eunice", 101)
member2 = Member("Evans", 102)
member3 = Member("Anne", 103)

#library structure (books, members):
library = Library([], []) #create an empty library object
#add books and members to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_member(member1)
library.register_member(member2)
library.register_member(member3)

#find book and member
library.find_book(1)
library.find_member(102)

#borrow book
library.borrow_book(102, 2)

#return book
library.return_book(102, 2)
print(library)  # Print state of the library
