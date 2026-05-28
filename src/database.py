import sqlite3

def create_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # User table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )''')

    # Prediction history
    c.execute('''CREATE TABLE IF NOT EXISTS history (
                    username TEXT,
                    prediction REAL
                )''')

    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = c.fetchall()
    conn.close()
    return data

def add_history(username, prediction):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO history VALUES (?, ?)", (username, prediction))
    conn.commit()
    conn.close()

def get_history(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT prediction FROM history WHERE username=?", (username,))
    data = c.fetchall()
    conn.close()
    return data