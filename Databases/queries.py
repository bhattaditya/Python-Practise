import sqlite3

connection = sqlite3.connect('mystore.db')
cursor = connection.cursor()

query = "Select * from User"
cursor.execute(query)
print(cursor.fetchall())


