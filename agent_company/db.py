import sqlite3

conn = sqlite3.connect("company.db", check_same_thread=False)
conn.execute("CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY, message TEXT)")
conn.commit()

def add_activity(message):
    conn.execute("INSERT INTO activities(message) VALUES (?)", (message,))
    conn.commit()

def get_activities():
    return conn.execute("SELECT message FROM activities ORDER BY id DESC").fetchall()
