# coding: utf-8
#***import
import nltk
import sys
import os.path
import re
import sqlite3

db = sqlite3.connect('_googlePgsDb.sqlite') #put this up here so I'm not continually opening and closing the database with every file in the folder I loop through.
#***open files with a loop WITH statement that will close them after it is done
#test folder with 5 google html files is desktop/gHtmlTestFolder

folder = '/Users/robertmckee/Tresors/Projects/InvalidPatents/1stFileGoogle'
ginput_fileList = os.listdir(folder) #creats list of files in folder
#with open (ginput_file, "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
#    text=myfile.read()
#raw = nltk.clean_html(text)
counter = 0
lensUrlListFile = open('/Users/robertmckee/Tresors/Projects/InvalidPatentFiles/_LensUrlList.txt',"a")
for file in ginput_fileList:
  file_name = '/Users/robertmckee/Tresors/Projects/InvalidPatents/1stFileGoogle/' + file
  with open(file_name, 'r') as myfile:
    text = myfile.read()
  raw = nltk.clean_html(text)
  #print file_name  #prints each file name. loops through each file in folder.

#***parse the files to get pubNum assignee and if cancelled claims
  #**pubNum
  int_pubNum = raw.partition('Publication number ')
  pubNumStr = int_pubNum[2].partition('Publication type')
  pubNumUS = pubNumStr[0].partition('US') #just partitioning out the number
  pubNumNum = pubNumUS[2].partition(' ')
  pubNumLast = pubNumNum[2].partition('Publication')
  pubNum = pubNumUS[1]+'_'+pubNumNum[0]+'_'+pubNumLast[0]
  print int_pubNum[1]+pubNum
  lensUrlListFile.write(pubNum+'\n') #the '\n' causes it to do a new line.
  patNum = pubNumNum[0]

  #**filing date [filingDat]
  int_filingDat = raw.partition('Filing date ')
  int_filingDatMnth = int_filingDat[2].partition(' ')
  int_filingDatDay = int_filingDatMnth[2].partition(', ')
  int_filingDatYr = int_filingDatDay[2].partition('Priority date')
  filingDat = int_filingDat[1]+int_filingDatYr[0]+' '+int_filingDatMnth[0]+' '+int_filingDatDay[0]
  #print filingDat
  filingDatYr = int_filingDatYr[0]
  filingDatMnth = int_filingDatMnth[0]
  filingDatDay = int_filingDatDay[0]


  #**assgnee
  int_assgnee = int_filingDatYr[2].partition('Original Assignee ')
  assgneeName = int_assgnee[2].partition('Export')
  assgnee = assgneeName[0]
  #print int_assgnee[1]+assgnee

  #**canceled or cancelled
  int_legalEventsString = assgneeName[2].partition('Legal Events')
  legalEventsString = int_legalEventsString[2].partition('Legal Events')
  matchCanceled = re.search(r"(canceled|cancelled|CANCELED|CANCELLED)", legalEventsString[2]) #the '|' separates possibilites it could be http://flockhart.virtualave.net/RBIF0100/regexp.html
  if matchCanceled:
    cancledClaims = 'Yes'
    print 'Canceled Claims!'
  elif len(legalEventsString[2])<1:
    cancledClaims = 'Verify'
    print 'No Legal Events Available! Check!'
  else:
    cancledClaims = 'No'
    print 'No Canceled Claims'
#***create/write/append to a txt file for url list of lens.org scraping
  #already done further up


#*** write to a database
  db.text_factory = str
  cursor = db.cursor()
  cursor.execute('insert into patent values (?,?,?,?,?,?,?,?)',(pubNum, assgnee, filingDatYr, filingDatMnth, filingDatDay, cancledClaims, file_name, patNum))
  db.commit()
  counter += 1
  print 'Files processed so far: ', counter
#file_name
#pubNumNum  #this is the patent number that I used to find them in google
#pubNum  #This is the critical one I'm looking for
#int_filingDatYr
#int_filingDatMnth
#int_filingDatDay
#assgnee
#cancledClaims

#*** close database and listfile when the loop is over. so keep it against the left side. no indents.
print 'Total Number of files processed: ', counter
lensUrlListFile.close()
db.close()
