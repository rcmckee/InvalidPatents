#using the SQLite Module
import sqlite3
#connecting SQLite to the database
db = sqlite3.connect('_ipDatabase')

#creating (CREATE) and deleting (DROP) tables using cursor
cursor = db.cursor()
cursor.execute('''
	CREATE TABLE patent(id INTERGER PRIMARY KEY, pubNum TEXT unique, title TEXT, patNum TEXT, inventors TEXT, assgnee TEXT, filingDat TEXT, intlClass TEXT, usaClass TEXT, fieldSrch TEXT, primEx TEXT, assEx TEXT, atnyAgntFirm TEXT, abst TEXT, spec TEXT, claim1 TEXT, claim2 TEXT, claim3 TEXT, claim4 TEXT, claim5 TEXT, claim6 TEXT, claim7 TEXT, claim8 TEXT, claim9 TEXT, claim10 TEXT, claim11 TEXT, claim12 TEXT, claim13 TEXT, claim14 TEXT, claim15 TEXT, claim16 TEXT, claim17 TEXT, claim18 TEXT, claim19 TEXT, claim20 TEXT, regInfo TEXT, draftingAtny TEXT, lawSchool TEXT, issueStat TEXT)
 ''')
#update database records
db.commit()
###########**************maybe only have this one time then don't need it? I wouldn't want to keep creating columns each time I run the program.









#to insert data use cursor. If you need values from python variables it is recommended to use the "?" placeholder. Never use string operations or concatenations to make your queries because it is very insecure.
#**************this code would go into the parsing program.


#_parsing.py code
#parsing lens full text first
#enter into database
#then parsing lens reg info
#enter into database
#then parsing somehow the drafting attorney info
#enter into database
#should I only enter into database once?

#insert parsed information
#opens the database
db = sqlite3.connect('_ipDatabase')
#makes the connection to it
cursor = db.cursor()
cursor.execute(''' INSERT INTO patent(pubNum, title, patNum, inventors, assgnee, filingDat, intlClass, usaClass, fieldSrch, primEx, assEx, atnyAgntFirm, abst, spec, claim1, claim2, claim3, claim4, claim5, claim6, claim7, claim8, claim9, claim10, claim11, claim12, claim13, claim14 , claim15, claim16, claim17, claim18, claim19, claim20, regInfo, draftingAtny, lawSchool, issueStat)
					VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (pubNum, title, patNum, inventors, assgnee, filingDat, intlClass, usaClass, fieldSrch, primEx, assEx, atnyAgntFirm, abst, spec, claim1, claim2, claim3, claim4, claim5, claim6, claim7, claim8, claim9, claim10, claim11, claim12, claim13, claim14 , claim15, claim16, claim17, claim18, claim19, claim20, regInfo, draftingAtny, lawSchool, issueStat))

print pubNum+ ' inserted into database.'
print 'last row id: %d' % id
#when done working with the db you have to close the connection
db.close()
