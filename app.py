import tkinter as tk
from tkinter import messagebox, simpledialog
from library import Library
from models import Book, Member

library = Library()  # Your existing Library class

# -------------------- Main Window --------------------
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x400")

# -------------------- Helper Functions --------------------
def add_book_gui():
    title = simpledialog.askstring("Add Book", "Enter book title:")
    if not title:
        return
    author = simpledialog.askstring("Add Book", "Enter author name:")
    if not author:
        return
    book_no = simpledialog.askstring("Add Book", "Enter book number:")
    if not book_no:
        return

    book = Book(title, author, book_no)
    library.add_book(book)
    messagebox.showinfo("Success", f"Book '{title}' added!")

def register_member_gui():
    name = simpledialog.askstring("Register Member", "Enter member name:")
    if not name:
        return
    member_id = simpledialog.askstring("Register Member", "Enter member ID:")
    if not member_id:
        return

    member = Member(member_id, name)
    library.register_member(member)
    messagebox.showinfo("Success", f"Member '{name}' registered!")

def borrow_book_gui():
    member_id = simpledialog.askstring("Borrow Book", "Enter member ID:")
    if not member_id:
        return
    book_no = simpledialog.askstring("Borrow Book", "Enter book number:")
    if not book_no:
        return
    library.borrow_book(member_id, book_no)

def return_book_gui():
    member_id = simpledialog.askstring("Return Book", "Enter member ID:")
    if not member_id:
        return
    book_no = simpledialog.askstring("Return Book", "Enter book number:")
    if not book_no:
        return
    library.return_book(member_id, book_no)

def view_books_gui():
    books = library.get_all_books()
    if not books:
        messagebox.showinfo("Books", "No books in library.")
        return
    book_list = "\n".join([f"{b.book_no}: {b.title} by {b.author} ({b.status})" for b in books])
    messagebox.showinfo("Books in Library", book_list)

def view_members_gui():
    members = library.get_all_members()
    if not members:
        messagebox.showinfo("Members", "No members registered.")
        return
    member_list = "\n".join([f"{m.member_id}: {m.name} | Borrowed: {', '.join(m.borrowed_books) if m.borrowed_books else 'None'}" for m in members])
    messagebox.showinfo("Library Members", member_list)

# -------------------- Buttons --------------------
tk.Button(root, text="Add Book", width=20, command=add_book_gui).pack(pady=5)
tk.Button(root, text="Register Member", width=20, command=register_member_gui).pack(pady=5)
tk.Button(root, text="Borrow Book", width=20, command=borrow_book_gui).pack(pady=5)
tk.Button(root, text="Return Book", width=20, command=return_book_gui).pack(pady=5)
tk.Button(root, text="View All Books", width=20, command=view_books_gui).pack(pady=5)
tk.Button(root, text="View All Members", width=20, command=view_members_gui).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=5)

# -------------------- Run GUI --------------------
root.mainloop()
