import sqlite3

DB_PATH = "URL-shortener/urls.db" 

def conn_to_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def add_short_code(url, code):
    conn = conn_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO urls VALUES(?,?,?);", (None, code, url))
    conn.commit()
    conn.close()

def init_db():
    conn = conn_to_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS urls(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_code TEXT UNIQUE DEFAULT NULL,
        original_url TEXT UNIQUE NOT NULL,
        clicks INT DEFAULT 0);
    """)

    # urls = [(None, None, '/example.com/very/long/url/1'), (None, None, '/example.com/very/long/url/2')]
    # cur.executemany("INSERT OR IGNORE INTO urls VALUES(?, ?, ?);", urls)

    conn.commit()
    conn.close()