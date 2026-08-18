import sqlite3

conn=sqlite3.connect('company.db', check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS activities(id INTEGER PRIMARY KEY,message TEXT)')
conn.commit()

def add_activity(msg):
    conn.execute('INSERT INTO activities(message) VALUES(?)',(msg,))
    conn.commit()

def get_activities():
    return [x[0] for x in conn.execute('SELECT message FROM activities ORDER BY id DESC').fetchall()]
