import sqlite3
#connecting SQLite to the database
db = sqlite3.connect('_ipDatabase')

#creating (CREATE) and deleting (DROP) tables using cursor
cursor = db.cursor()
cursor.execute('''
	CREATE TABLE patent(id INTERGER PRIMARY KEY, pubNum TEXT unique, title TEXT, patNum TEXT, inventors TEXT, assgnee TEXT, filingDat TEXT, intlClass TEXT, usaClass TEXT, fieldSrch TEXT, primEx TEXT, assEx TEXT, atnyAgntFirm TEXT, abst TEXT, spec TEXT, claim1 TEXT, claim2 TEXT, claim3 TEXT, claim4 TEXT, claim5 TEXT, claim6 TEXT, claim7 TEXT, claim8 TEXT, claim9 TEXT, claim10 TEXT, claim11 TEXT, claim12 TEXT, claim13 TEXT, claim14 TEXT, claim15 TEXT, claim16 TEXT, claim17 TEXT, claim18 TEXT, claim19 TEXT, claim20 TEXT, regInfo TEXT, draftingAtny TEXT, lawSchool TEXT, issueStat TEXT)
 ''')
#when done working with the db you have to close the connection
db.close()
