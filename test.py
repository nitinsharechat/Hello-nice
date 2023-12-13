import os
import sqlite3

def login(username, password):
    # Connect to the database (SQLite in this case)
    conn = sqlite3.connect(':memory:')  # Using in-memory database for simplicity
    cursor = conn.cursor()

    # Create a basic users table for demonstration
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

    # Insert a user (vulnerable code)
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")

    # Attempt to authenticate user (vulnerable code)
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    user = cursor.fetchone()

    # Close the database connection
    conn.close()

    return user

# Example usage (vulnerable code)
result = login("admin' OR '1'='1' --", "password")
if result:
    print("Login successful!")
else:
    print("Login failed.")
