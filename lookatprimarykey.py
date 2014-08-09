import sqlite3
#connecting SQLite to the database
db = sqlite3.connect('lookatprimarykey')

#creating (CREATE) and deleting (DROP) tables using cursor
cursor = db.cursor()
cursor.execute('CREATE TABLE patent(id INTERGER PRIMARY KEY, who)')
#update database records
db.commit()
db.close()