import sqlite3
import os

os.system("rm database.db")
os.system("touch database.db")

conn = sqlite3.connect('database.db')
print("Connected to database scucessfully")

# add players entity to database
conn.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
''')

#conn.execute("CREATE TABLE players (id integer primary key autoincrement, first_name TEXT, last_name TEXT)")
print("Created entity players succesfully!")

# add team entity to database
conn.execute("CREATE TABLE teams (id integer primary key autoincrement, name TEXT)") 
print("Created entity teams successfully!")

conn.close()