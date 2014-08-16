# coding: utf-8
#***import
import nltk
import sys
import os.path
import re


#***open files with a loop WITH statement that will close them after it is done
#test folder with 5 google html files is desktop/gHtmlTestFolder
folder = '/Users/robertmckee/Desktop/gHtmlTestFolder'
ginput_fileList = os.listdir(folder) #creats list of files in folder
#with open (ginput_file, "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
#    text=myfile.read()
#raw = nltk.clean_html(text)

for file in ginput_fileList:
  file_name = '/Users/robertmckee/Desktop/gHtmlTestFolder/' + file
  with open(file_name, 'r') as myfile:
    text = myfile.read()
  raw = nltk.clean_html(text)
  print file_name  #prints each file name. loops through each file in folder.

#***parse the files to get pubNum assignee and if cancelled claims
  #**pubNum
  int_pubNum = raw.partition('Publication number ')
  pubNumStr = int_pubNum[2].partition('Publication type')
  pubNumUS = pubNumStr[0].partition('US') #just partitioning out the number
  pubNumNum = pubNumUS[2].partition(' ')
  pubNumLast = pubNumNum[2].partition('Publication')
  pubNum = pubNumUS[1]+'_'+pubNumNum[0]+'_'+pubNumLast[0]
  print int_pubNum[1]+pubNum

  #**assgnee
  int_assgnee = raw.partition('Original Assignee ')
  assgneeName = int_assgnee[2].partition('Export')
  assgnee = assgneeName[0]
  print int_assgnee[1]+assgnee

  #**canceled or cancelled
  int_legalEventsString = assgneeName[2].partition('Legal Events')
  legalEventsString = int_legalEventsString[2].partition('Legal Events')
 # if len(legalEventsString[2]) < 1:
 #   print 'No Legal Information'
 # elif re.search('canceled', legalEventsString[2], re.IGNORECASE) == Match:
 #   print 'Canceled Claims'
 # elif re.search('cancelled', legalEventsString[2], re.IGNORECASE) == Match:
 #   print 'Canceled Claims'
 # else:
 #   print 'No Canceled Claims'
 # if re.search('Legal Events', legalEventsString[1], re.IGNORECASE) == False:
 #   print 'No Legal Events available'
 # if len(legalEventsString[2])<1:
 #   print 'No Legal Events Available! Check!'
  matchCanceled = re.search(r"(canceled|cancelled|CANCELED|CANCELLED)", legalEventsString[2]) #the '|' separates possibilites it could be http://flockhart.virtualave.net/RBIF0100/regexp.html
  if matchCanceled:
    print 'Canceled Claims!'
  elif len(legalEventsString[2])<1:
    print 'No Legal Events Available! Check!'
  else:
    print 'No Canceled Claims'
#***create/write/append to a txt file or database?


#***