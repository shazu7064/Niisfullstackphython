import sqlite3

# connect to database
conn = sqlite3.connect("student.db")

# create cursor
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# insert data
cur.execute("INSERT INTO student VALUES(1,'Ravi',85)")

# save changes
conn.commit()

# close connection
conn.close()

print("Data inserted successfully")