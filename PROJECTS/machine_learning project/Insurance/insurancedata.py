import sqlite3

data_insert_query = """
INSERT INTO project (age, gender, bmi, children, region, smoker, health, prediction)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

def create_table():
    conn = sqlite3.connect('insurance.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS project (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        gender INTEGER,
        bmi REAL,
        children INTEGER,
        region TEXT,
        smoker INTEGER,
        health INTEGER,
        prediction REAL
    )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect('insurance.db')
    cur = conn.cursor()
    cur.execute(data_insert_query, data)
    conn.commit()
    cur.close()
    conn.close()
