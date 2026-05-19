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