# Tranzaksiya - bir nechta sql querylarning birgalikda ishlashi,
# agar biri ishlamasa barchasi rollback bo'lishi.

# ACID - Atomicity, Consistency, Isolation, Durability
# Atomicity - Bo'linmaslik
# Consistency - Moslik
# Isolation - Izolatsiya
# Durability - Davomiylik(Doimiylik)

import sqlite3

conn = sqlite3.connect("my_transactions.db")
cursor = conn.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS accounts(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     balance REAL NOT NULL
# );
# """)
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS transactions(
#     id INTEGER PRIMARY KEY,
#     from_account_id INTEGER,
#     to_account_id INTEGER,
#     amount REAL NOT NULL,
#     FOREIGN KEY (from_account_id) REFERENCES accounts (id),
#     FOREIGN KEY (to_account_id) REFERENCES accounts (id)
# );
# """)
#
# cursor.execute("""INSERT INTO accounts(name, balance) VALUES ('Alice',1000);""")
# cursor.execute("""INSERT INTO accounts(name, balance) VALUES ('Bob',500);""")

try:
    cursor.execute("BEGIN;")
    cursor.execute("""INSERT INTO transactions (from_account_id, to_account_id, amount) 
                        VALUES (1,2,100);""")
    cursor.execute("""UPDATE accounts SET balance = balance - 100 WHERE id=1;""")
    cursor.execute("""UPDATE accounts SET balance = balance + 100 WHERE id=2;""")
    conn.commit()
except sqlite3.Error as e:
    print(f"Xatolik chiqdi: {e}")
    conn.rollback()
cursor.close()

conn.close()
