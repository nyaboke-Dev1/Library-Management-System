📚 Library Management System
A comprehensive Python-based library management system that enables efficient management of books, members, and borrowing transactions. This project demonstrates proficiency in Object-Oriented Programming (OOP), data persistence, and database integration.
🎯 Project Overview
This Library Management System is designed to handle core library operations including book cataloging, member registration, borrowing and returning books, and generating various reports. The system supports both file-based storage and MySQL database integration for robust data management.
✨ Features
Core Functionality

Book Management

Add, update, and remove books from the catalog
Track book details (title, author, ISBN, quantity, availability)
Search books by title, author, or ISBN


Member Management

Register new library members
Update member information
Track member borrowing history
Enforce borrowing limits per member


Borrowing System

Issue books to members
Process book returns
Automatic date tracking for borrow/return transactions
Calculate and manage overdue books


Search & Reporting

Search functionality for books and members
View all available books
View all borrowed books
Generate member activity reports
Track borrowing statistics



Technical Features

Object-Oriented Programming design
Dual data persistence (File-based and MySQL)
Comprehensive error handling and validation
Command-line interface (CLI)
Data synchronization between storage methods

🛠️ Technologies Used

Python 3.x
MySQL - Database management
File I/O - JSON/CSV for data persistence
datetime - Date and time tracking
mysql-connector-python - MySQL database connectivity

📋 Prerequisites
Before running this project, ensure you have the following installed:
bash- Python 3.8 or higher
- MySQL Server 8.0 or higher
- pip (Python package manager)
🚀 Installation

Clone the repository

bash   git clone https://github.com/nyaboke-Dev1/library-management-system.git
   cd library-management-system

Create a virtual environment (recommended)

bash   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required dependencies

bash   pip install -r requirements.txt

Set up MySQL Database

bash   # Log into MySQL
   mysql -u root -p
   
   # Create database
   CREATE DATABASE library_db;

Configure database connection

Copy config.example.py to config.py
Update database credentials in config.py:



python     DB_CONFIG = {
         'host': 'localhost',
         'user': 'your_username',
         'password': 'your_password',
         'database': 'library_db'
     }

Initialize the database

bash   python setup_database.py
💻 Usage
Starting the Application
bashpython main.py
Example Operations
Adding a Book
Select option: 1 (Add Book)
Enter title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter ISBN: 978-0-7432-7356-5
Enter quantity: 3
Registering a Member
Select option: 2 (Register Member)
Enter name: John Doe
Enter email: john.doe@example.com
Enter phone: +254-123-456-789
Borrowing a Book
Select option: 3 (Borrow Book)
Enter member ID: M001
Enter book ISBN: 978-0-7432-7356-5
Searching for Books
Select option: 7 (Search Books)
Search by (title/author/isbn): title
Enter search term: Gatsby
📁 Project Structure
library-management-system/
│
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── setup_database.py      # Database initialization script
│
├── models/
│   ├── __init__.py
│   ├── book.py           # Book class
│   ├── member.py         # Member class
│   └── transaction.py    # Transaction class
│
├── services/
│   ├── __init__.py
│   ├── library_service.py    # Core business logic
│   ├── file_handler.py       # File operations
│   └── db_handler.py         # Database operations
│
├── utils/
│   ├── __init__.py
│   ├── validators.py         # Input validation
│   └── helpers.py            # Utility functions
│
├── data/                     # File-based storage (JSON/CSV)
│   ├── books.json
│   ├── members.json
│   └── transactions.json
│
└── tests/                    # Unit tests
    ├── __init__.py
    ├── test_book.py
    ├── test_member.py
    └── test_library_service.py
🎓 Learning Objectives
This project demonstrates:

Object-Oriented Programming: Classes, inheritance, encapsulation
Data Persistence: File I/O and database management
Error Handling: Comprehensive exception handling
CRUD Operations: Create, Read, Update, Delete functionality
Data Validation: Input validation and data integrity
Database Integration: MySQL connectivity and queries
Software Design: Modular architecture and separation of concerns

🔮 Future Enhancements

 GUI interface using Tkinter
 Web-based version using Flask
 Fine calculation for overdue books
 Email notifications for due dates
 Book reservation system
 User authentication and role-based access
 Export reports to PDF/Excel
 RESTful API integration

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
📝 License
This project is MIT licensed.
👤 Author
Eunice Nyaboke

GitHub: @nyaboke-Dev1
LinkedIn: Eunice Nyaboke Onkundi
Email: enyaboke399@gmail.com