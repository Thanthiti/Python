import sqlite3

connect = sqlite3.connect("SQL/chinook.db")
print("Connect to Db")
w = connect.execute("SELECT * FROM customers")

for rows in w:
    print(rows)
