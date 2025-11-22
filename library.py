import sqlite3
import json
from models import Book, Member
import os
DB_FILE = os.path.join(os.path.dirname(__file__), "library.db")
class Library:
    def connect(self):
        """Creates a connection to the SQLite database."""
        return sqlite3.connect(DB_FILE)

    # ------------------ BOOK METHODS ------------------

    def add_book(self, book: Book):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
                            (book.book_no, book.title, book.author, book.status))
            conn.commit()
            print("Book added successfully!")
        except sqlite3.IntegrityError:
            print("A book with that number already exists.")
        conn.close()

    def find_book(self, book_no):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books WHERE book_no=?", (book_no,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Book(row[1], row[2], row[0], row[3])
        return None

    def get_all_books(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()

        return [Book(row[1], row[2], row[0], row[3]) for row in rows]

    # ------------------ MEMBER METHODS ------------------

    def register_member(self, member: Member):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO members VALUES (?, ?, ?)",
                            (member.member_id, member.name, json.dumps([])))
            conn.commit()
            print("Member registered successfully!")
        except sqlite3.IntegrityError:
            print("A member with that ID already exists.")
        conn.close()

    def find_member(self, member_id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM members WHERE member_id=?", (member_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            borrowed = json.loads(row[2])
            return Member(row[0], row[1], borrowed)

        return None
    def get_all_members(self):
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()
        conn.close()
        return [Member(row[0], row[1], json.loads(row[2])) for row in rows]
    def delete_member(self, member_id):
        conn = self.connect()
        cursor = conn.cursor()
        # Check if the member exists first
        cursor.execute("SELECT * FROM members WHERE member_id=?", (member_id,))
        if not cursor.fetchone():
            print(f"No member found with ID {member_id}.")
            conn.close()
            return

        cursor.execute("DELETE FROM members WHERE member_id=?", (member_id,))
        conn.commit()
        conn.close()

        print(f"Member with ID {member_id} has been deleted successfully!")


    # ------------------ BORROW / RETURN ------------------

    def borrow_book(self, member_id, book_no):
      member = self.find_member(member_id)  # fetch fresh
      book = self.find_book(book_no)        # fetch fresh

      if not member:
          print("Member not found.")
          return
      if not book:
          print("Book not found.")
          return
      if not book.is_available():
          print("Book is already borrowed.")
          return
      if not member.can_borrow():
          print("Member already has 3 books.")
          return

      # Update book status in DB and in-memory object
      conn = self.connect()
      cursor = conn.cursor()
      cursor.execute("UPDATE books SET status='borrowed' WHERE book_no=?", (book_no,))
      book.status = "borrowed"

      # Update member borrowed_books in DB and in-memory object
      member.borrowed_books.append(book_no)
      cursor.execute("UPDATE members SET borrowed_books=? WHERE member_id=?",
                  (json.dumps(member.borrowed_books), member_id))

      conn.commit()
      conn.close()

      print(f"{member.name} borrowed '{book.title}' successfully!")


    def return_book(self, member_id, book_no):
        member = self.find_member(member_id)
        book = self.find_book(book_no)

        if not member or not book:
            print("Invalid member or book.")
            return

        if book_no not in member.borrowed_books:
            print("This member did not borrow that book.")
            return

        conn = self.connect()
        cursor = conn.cursor()

        # Update book status to available
        cursor.execute("UPDATE books SET status=? WHERE book_no=?",
                        ("available", book_no))

        # Update member borrowed books list
        member.borrowed_books.remove(book_no)
        cursor.execute("UPDATE members SET borrowed_books=? WHERE member_id=?",
                        (json.dumps(member.borrowed_books), member_id))

        conn.commit()
        conn.close()

        print(f"{member.name} returned '{book.title}' successfully!")
