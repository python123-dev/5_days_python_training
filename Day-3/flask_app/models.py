#Flask Database Handling - a small SQLite helper module
#SQLite needs no server, the .db file is created next to this script on first run
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'customers.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   #lets us access columns by name, e.g. row['name']
    return conn


def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def get_all_customers():
    conn = get_db()
    rows = conn.execute('SELECT * FROM customers').fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_customer(customer_id):
    conn = get_db()
    row = conn.execute('SELECT * FROM customers WHERE id = ?', (customer_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def add_customer(name, address):
    conn = get_db()
    cursor = conn.execute('INSERT INTO customers (name, address) VALUES (?, ?)', (name, address))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def delete_customer(customer_id):
    conn = get_db()
    conn.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()
