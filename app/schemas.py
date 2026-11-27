import json
from database import conn_to_db, add_short_code
import secrets
import string

ALPHABET = string.ascii_letters + string.digits

def get_all_short_code():
    conn = conn_to_db()
    cur = conn.cursor()
    cur.execute("SELECT short_code FROM urls;")
    allShortCodes = cur.fetchall()
    conn.close()
    return allShortCodes

def set_new_code(url):
    code = generate_short_code()
    allShortCodes = get_all_short_code()
    for i in allShortCodes:
        if i == allShortCodes:
            return
        else: 
            add_short_code(url, code)
            return code

def generate_short_code(length: int = 5) -> str:
    return ''.join(secrets.choice(ALPHABET) for _ in range(length))       