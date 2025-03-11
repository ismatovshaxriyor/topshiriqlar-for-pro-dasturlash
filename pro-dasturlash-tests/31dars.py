import sqlite3 as sq

conn = sq.connect("sample-database.db")
cur = conn.cursor()

cur.execute("""
SELECT * FROM employees LIMIT 5;
""")
ans = cur.fetchall()
for i in ans:
    print(i)

cur.close()
conn.close()