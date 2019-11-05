import sqlite3
conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
try:
    cur.execute("""
        CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
except sqlite3.OperationalError:  # error
    pass

l = [(None, "Rounak"), (None, "Saif"), (None, "Ro"), (None, "Roun")]

for item in l:
    cur.execute("INSERT INTO users VALUES(?, ?)", item)

cur.execute("SELECT * FROM users")

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchall())

conn.commit()  # if not not saved in db
cur.close()

"""
run two times

(1, 'Rounak')
(2, 'Saif')
[(3, 'Ro'), (4, 'Roun'), (5, 'Rounak'), (6, 'Saif'), (7, 'Ro'), (8, 'Roun')]

""""
