import sqlite3

# connect to database
conn = sqlite3.connect("student.db")

# create cursor
cur = conn.cursor()

# fetch data
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

# display data
for r in rows:
    print(r)

# close connection
conn.close()