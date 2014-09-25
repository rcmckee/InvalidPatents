# coding: utf-8
#***import
import nltk
import sys
import os.path
import re

#********Read folder and generate list of files in folder to loop through
folder = '/Users/robertmckee/Tresors/Projects/InvalidPatentFiles/lensFullTextFiles'
ginput_fileList = os.listdir(folder) #creats list of files in folder
error_counter = 0
counter = 0
errorUrlListFile = open('/Users/robertmckee/Tresors/Projects/InvalidPatentFiles/_errorUrlList.txt',"a") #file to write to
for file in ginput_fileList:
  file_name = '/Users/robertmckee/Tresors/Projects/InvalidPatentFiles/lensFullTextFiles/' + file
  with open(file_name, 'r') as myfile:
    text = myfile.read()
  raw = nltk.clean_html(text)


  #*********Check for errors & write to _errorUrlList.txt the name of the file that is an error

  #int_legalEventsString = assgneeName[2].partition('Legal Events')
  #legalEventsString = int_legalEventsString[2].partition('Legal Events')
  matchPositive = re.search(r"(Legal events|Abstract)", raw) #the '|' separates possibilites it could be http://flockhart.virtualave.net/RBIF0100/regexp.html
  if matchPositive:
    error = 'No error'
    print error
  else:
    error = 'ERROR!!!!'
    error_counter += 1
    errorUrlListFile.write(file+'\n') #the '\n' causes it to do a new line. #this is writing it to list file.

    print error
  ####reginfo
  #check for files that say error or trouble downloading.

  #look for "Oops, something went wrong" (ignore case)
  #nothing after "guess work area"
  #look for "Legal events" (ignore case) as a positive that it worked

  #####fulltext
  #"information currently unavailable" ignore case
  #look for "Abstract" as a postive that it worked


  counter += 1
  print 'Files processed so far: ', counter

#*** close database and listfile when the loop is over. so keep it against the left side. no indents.
print 'Total Number of files processed: ', counter
print 'Total Number of files with errors: ', error_counter
errorUrlListFile.close()  #close the list file after you are done with it. But don't close it each time you do the loop. Just after the loop is done running. Don't want to keep closing and opening the file.
