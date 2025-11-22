class Book:
    def __init__(self, title, author, book_no, status="available"):
        self.title = title
        self.author = author
        self.book_no = book_no
        self.status = status
    #helper method to check availability
    def is_available(self):
        return self.status == "available"
    
    #method to borrow book
    def borrow(self):
        if self.is_available():
            self.status = "borrowed"
            print(f"You have borrowed {self.title} by {self.author}")
        else:
            print(f"Sorry, {self.title} is already borrowed.")
    
    #method to return book
    def return_book(self):
        if not self.is_available():
            self.status="available"
            print(f"You have returned {self.title} by {self.author}")
        else:
            print(f"{self.title} was never borrowed.")
    
    #method to check book status       
    def book_status(self):
        print(f"Status of {self.title}: {self.status}")
    
    #method to print book details
    def __str__(self):
        return(f"Book Title: {self.title}, Author: {self.author}, Book No: {self.book_no}")
    
class Member:
    MAX_BORROW_LIMIT = 3
    
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id 
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []  #create a new list for each memeber to store borrowed books
    #helper method to check if member can borrow more books
    def can_borrow(self):
        return len(self.borrowed_books) < self.MAX_BORROW_LIMIT #limit is 3 books
    
    #method to borrow book
    def borrow_book(self, book): 
        if self.can_borrow():
            return self.borrowed_books.append(book.book_no)
        else:
            print("Borrowing limit reached. Cannot borrow more books.")
        print(f"you have borrowed {book.title} by {book.author}") 
    
    #method for returning book
    def return_book(self, book): 
        if book.book_no in self.borrowed_books:
            self.borrowed_books.remove(book.book_no)
        else:
            print("This book was not borrowed by the member.")
        print(f"you have returned {book.title} by {book.author}")  
    #method to list borrowed books
    def borrowed_books_list(self):
        return [book.title for book in self.borrowed_books]
    #method to print member details  
    def __str__(self):
        return f"Member Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {self.borrowed_books_list()}" 