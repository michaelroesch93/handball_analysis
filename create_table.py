import sqlite3
import os

os.system("rm database.db")
os.system("touch database.db")

conn = sqlite3.connect('database.db')
print("Connected to database scucessfully")

# add players entity to database
conn.execute("CREATE TABLE players (first_name TEXT, last_name TEXT)")
print("Created entity players succesfully!")

# add team entity to database
conn.execute("CREATE TABLE teams (name TEXT)")
print("Created entity teams successfully!")

conn.close()