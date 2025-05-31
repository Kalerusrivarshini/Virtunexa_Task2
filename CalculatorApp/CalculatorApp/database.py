import sqlite3

def log_to_db(operation, a, b, result):
    conn = sqlite3.connect("calculator.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT,
            operand1 REAL,
            operand2 REAL,
            result TEXT
        )
    """)
    cursor.execute("INSERT INTO history (operation, operand1, operand2, result) VALUES (?, ?, ?, ?)",
                   (operation, a, b, str(result)))
    conn.commit()
    conn.close()
