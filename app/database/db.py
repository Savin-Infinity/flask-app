import sqlite3

DATABASE = "app/database/users.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    return conn


# This file is ONLY for connecting to the database.