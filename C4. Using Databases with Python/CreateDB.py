import sqlite3
import os

# Define database path
db_path = os.path.join(os.getcwd(), "my_database.db")

# Create a connection (this will create the database file if it doesn't exist)
conn = sqlite3.connect(db_path)

# Optional: create a simple table
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"Database created at: {db_path}")
