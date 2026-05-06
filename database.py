import sqlite3

conn = sqlite3.connect("gold_system.db", check_same_thread=False)
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    debt REAL DEFAULT 0
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    type TEXT,
    total REAL,
    paid REAL,
    notes TEXT,
    created_at TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS invoice_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER,
    piece_type TEXT,
    weight REAL,
    karat TEXT,
    raw_price REAL,
    wage REAL,
    total REAL,
    profit REAL
)
''')

conn.commit()
