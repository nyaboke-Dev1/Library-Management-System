# Library-Management-System
## Project Title
Library Management System Using Python (OOP, File Handling, Functions, and Basic Database Concepts)

## Problem Statement
Managing books manually in small libraries or study centers is often inefficient and prone to mistakes. Common issues include:

- Difficulty in tracking available and borrowed books  
- Mismanagement of member information  
- Absence of borrowing and return history  
- Lack of a centralized system for storing and updating records  

This project aims to create a simple and beginner-friendly Python-based Library Management System that addresses these issues using core Python concepts.

---

## Objectives
- Create a menu-driven library system using Python.
- Implement classes for Book, Member, and Library (OOP).
- Enable users to add books, register members, borrow, and return books.
- Store library data using file handling (text/JSON/CSV).
- Use exception handling to manage invalid inputs and errors.
- Integrate a simple MySQL database .
- Practice Python basics: loops, conditionals, lists, dictionaries, functions, and modules.

---

## Dataset Description
This project uses self-generated data through user input. However, data is stored in files for persistence.

### Stored Files:
- `books.json` – stores book details  
- `members.json` – stores member details  
- `transactions.txt` – stores borrowing and return history

### Example Book Fields:
- `book_no`  
- `title`  
- `author`  
- `status` (Available / Borrowed)

### Example Member Fields:
- `member_id`  
- `name`  
- `borrowed_books` (list)


## Tools and Technologies Used
### Programming Language
- Python 3

### Python Concepts
- Variables, input/output  
- Operators, loops, conditionals  
- Functions, lambda, map/filter  
- OOP (classes, objects, inheritance, encapsulation, polymorphism)  
- Collections (list, dictionary, set, tuple)  
- File handling (read/write, append)  
- Exception handling  
- Modules and packages  

### Optional Technologies
- MySQL or MongoDB  
- JSON module

## Proposed Methodology / Approach

### Phase 1 - System Design
- Identify classes: Book, Member, Library  
- Define methods: add_book(), register_member(), borrow_book(), return_book()  
- Decide on a storage method (file or database)

### Phase 2 - Implementation
1. **Create Book class**
   - title, author, book number, status  
2. **Create Member class**
   - name, member ID, borrowed books  
3. **Create Library class**
   - lists of books and members  
   - load and save data from files  
4. **Implement main.py**
   - menu-driven program  
   - call library methods  

### Phase 3 - File Handling
- Save books to a JSON file  
- Save members to a JSON file  
- Track borrow and return activities in `transactions.txt`

### Phase 4 - Testing & Exception Handling
- Handle invalid member IDs  
- Manage missing books  
- Prevent borrowing unavailable books  
- Handle empty inputs  

### Phase 5 -  Database Extension
- Create MySQL tables  
- Insert, select, and update books and members  


## Expected Outcomes
By the end of this project, I will have:

- A working Python Library Management System  
- Clean, well-structured OOP-based code  
- File storage for book and member data  
- Demonstrated understanding of Python fundamentals  
- MySQL integration  
