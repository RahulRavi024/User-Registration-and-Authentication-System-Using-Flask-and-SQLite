import sqlite3

connection = sqlite3.connect("app.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS auth_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

connection.commit()

connection.close()

print("Database created successfully!")