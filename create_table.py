import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database scucessfully")

conn.execute("CREATE TABLE players (first_name TEXT, last_name TEXT)")
print("Created table succesfully!")

conn.close()