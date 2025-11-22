class Member:
    MAX_BORROW_LIMIT = 3
    
    def __init__(self, name, member_id,):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  #create a new list for each memeber to store borrowed books
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