import sqlite3

conn =sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS 
    students (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER,
        grade FLOAT
    );
""")