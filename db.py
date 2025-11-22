import sqlite3
DB_FILE = "library.db"
def create_tables():
    conn = sqlite3.connect("DB_FILE")
    cursor = conn.cursor()

    # Create books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_no TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            status TEXT
        )
    """)

    # Create members table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id TEXT PRIMARY KEY,
            name TEXT,
            borrowed_books TEXT
        )
    """)

    conn.commit()
    conn.close()
