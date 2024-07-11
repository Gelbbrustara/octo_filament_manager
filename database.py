import sqlite3

def init_db():
    conn = sqlite3.connect('filament_manager.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS filaments (
            id INTEGER PRIMARY KEY,
            color TEXT,
            weight INTEGER,
            cost_per_kg REAL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS prints (
            id INTEGER PRIMARY KEY,
            name TEXT,
            filament_id INTEGER,
            weight INTEGER,
            date TEXT,
            FOREIGN KEY(filament_id) REFERENCES filaments(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_filament(color, weight, cost_per_kg):
    conn = sqlite3.connect('filament_manager.db')
    c = conn.cursor()
    c.execute('INSERT INTO filaments (color, weight, cost_per_kg) VALUES (?, ?, ?)', (color, weight, cost_per_kg))
    conn.commit()
    conn.close()

def add_print(name, filament_id, weight, date):
    conn = sqlite3.connect('filament_manager.db')
    c = conn.cursor()
    c.execute('INSERT INTO prints (name, filament_id, weight, date) VALUES (?, ?, ?, ?)', (name, filament_id, weight, date))
    conn.commit()
    conn.close()
