import sqlite3

connection = sqlite3.connect('mystore.db')
cursor = connection.cursor()
table_user = '''
                CREATE TABLE IF NOT EXISTS User(
                    id INTEGER PRIMARY KEY,
                    firstname TEXT,
                    lastname TEXT,
                    email TEXT
                )
            '''
cursor.execute(table_user)

connection.commit()
connection.close()