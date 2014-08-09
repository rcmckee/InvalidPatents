# coding: utf-8
import nltk
import re  #regex module in python and the uses of it http://www.regular-expressions.info/python.html
import sqlite3 # for info on using sqlite with python go to http://www.pythoncentral.io/introduction-to-sqlite-in-python/
#https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
#I could do a loop for a url list example https://stackoverflow.com/questions/18952351/scrape-html-files-stored-in-remote-directory
#with open ('lens-patent-US7469381B2-fulltext.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
	#text=myfile.read()
#test pages
#htmlonlyview-source www.lens.org lens patent US_7469381_B2 fulltext.html
#2ndtestpageview-source www.lens.org lens patent US_5612524_A fulltext.html

with open ('US_7469381_B2_fulltext.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read()   #need to use a file that is downloaded as a html only option
raw = nltk.clean_html(text)


#we have the code in text format. Now we have to process it. Lets partition it so we are continually working on a smaller block of text and are more precise.

pubNum = raw.partition(' - ')
print pubNum[0]+'test to see if printing pubNum'
title = pubNum[2].partition(' - \nThe Lens') #had to put in the \n for new line. otherwise it didn't recognize it and just returned the entire string. lets see how specific that is on other documents.
print title[0]+'test to see if printing title'
int_patNum = title[2].partition('(10)')#first break point
patNum = int_patNum[2].partition('\n')
print patNum[0]+'test to see if printing patNum'
int_inventors = patNum[2].partition('(75)')
inventors = int_inventors[2].partition('(73)')
print inventors[0]+'test to see if printing inventors'
assgnee = inventors[2].partition('Type')
print assgnee[0]+'test to see if printing assgnee'
int_filingDat = assgnee[2].partition('(22)')
filingDat = int_filingDat[2].partition('\n')
print filingDat[0]+'test to see if printing filingDat'
int_intlClass = filingDat[2].partition('(51)')
intlClass = int_intlClass[2].partition('(52)')
print intlClass[0]+'test to see if printing intlClass'
usaClass = intlClass[2].partition('(58)')
print usaClass[0]+'test to see if printing usaClass'
fieldSrch = usaClass[2].partition('(56)')
print fieldSrch[0]+'test to see if printing fieldSrch'
###########################################
#create if statement to look for Assistant Examiner or Art Unit use primeEx[2].len() if > 1 then there is something in the 3 tuple which means it found Assistant Examiner, otherwise go to Art Unit script

int_primEx = fieldSrch[2].partition('Primary Examiner') #2nd test, primary examiner prints out
primExAsEx = int_primEx[2].partition('Assistant Examiner')
s_primExAsEx = primExAsEx[2]
primEx = primExAsEx[2]  #make this so that the following else statement has a value to change  to change if no 'Assistant Examiner' is found
assEx = ' '
if len(s_primExAsEx) > 1:
	print int_primEx[1]+' '+primExAsEx[0] + 'test to see if this is actually printing out int_primEx if "Assistant Examiner" is found'
	assEx = primExAsEx[2].partition('Art Unit')
	print  primExAsEx[1]+assEx[0]+' test to see if printing assEx[0] when "Assistant Examiner" is found'


else:
	primExAU = int_primEx[2].partition('Art Unit')
	print primExAU[0]+' test to see if printing primExAU[0] when "Assistant Examiner" is not found'
	primEx = primExAU[2]

int_atnyAgntFirm = primEx.partition('Attorney, Agent, or Firm') #primEx is now a string not a tuble
s_int_atnyAgntFirm = int_atnyAgntFirm[2]
atnyAgntFirm = int_atnyAgntFirm[0]  # creating this variable so that the if statement has a global variable to change and I have a global variable to access. I can't figure out how to access a variable inside an if statement. That's stupid right?
#if no 'Attorney, Agent, or Firm' then atnyAgntFirm is a string, if there is 'Attorney, Agent, or Firm' then it's a turple so I need to change it to a string because the variable int_abst is looking for a string
if len(s_int_atnyAgntFirm) > 1:
	atnyAgntFirm = s_int_atnyAgntFirm.partition('(5')   #
	print atnyAgntFirm[0]+'test to see if printing atnyAgntFirm[0]'
	atnyAgntFirm = atnyAgntFirm[2]

int_abst = atnyAgntFirm.partition('7)')
abst = int_abst[2].partition('Draw')
print abst[0]+'test to see if printing abst'
int_spec = abst[2].partition('ng')
spec = int_spec[2].partition(' (57)')
#print spec[0]+'test to see if printing spec'
print spec[1] +"just during test to see if spec is printing but so I don't have to scroll up through the entire spec"
claim1 = spec[2].partition('2.')
print claim1[0]+'test to see if printing claim1' #this isn't printing

claim2 = claim1[2].partition('3.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim1[1]+claim2[0]+'test to see if printing claim2'
claim3 = claim2[2].partition('4.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim2[1]+claim3[0]+'test to see if printing claim3'
claim4 = claim3[2].partition('5.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim3[1]+claim4[0]+'test to see if printing claim4'
claim5 = claim4[2].partition('6.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim4[1]+claim5[0]+'test to see if printing claim5'
claim6 = claim5[2].partition('7.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim5[1]+claim6[0]+'test to see if printing claim6'
claim7 = claim6[2].partition('8.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim6[1]+claim7[0]+'test to see if printing claim7'
claim8 = claim7[2].partition('9.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim7[1]+claim8[0]+'test to see if printing claim8'
claim9 = claim8[2].partition('10.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim8[1]+claim9[0]+'test to see if printing claim9'
claim10 = claim9[2].partition('11.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim9[1]+claim10[0]+'test to see if printing claim10'
claim11 = claim10[2].partition('12.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim10[1]+claim11[0]+'test to see if printing claim11'
claim12 = claim11[2].partition('13.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim11[1]+claim12[0]+'test to see if printing claim12'
claim13 = claim12[2].partition('14.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim2[1]+claim13[0]+'test to see if printing claim13'
claim14 = claim13[2].partition('15.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim13[1]+claim14[0]+'test to see if printing claim14'
claim15 = claim14[2].partition('16.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim14[1]+claim15[0]+'test to see if printing claim15'
claim16 = claim15[2].partition('17.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim15[1]+claim16[0]+'test to see if printing claim16'
claim17 = claim16[2].partition('18.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim16[1]+claim17[0]+'test to see if printing claim17'
claim18 = claim17[2].partition('19.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim17[1]+claim18[0]+'test to see if printing claim18'
claim19 = claim18[2].partition('20.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim18[1]+claim19[0]+'test to see if printing claim19'
claim20 = claim19[2].partition('* * *')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim19[1]+claim20[0]+'test to see if printing claim20. If this appears after a later number it means that there was an error or that there were claims over 20'
#I need to loop this incase there is more than 20

draftingAtny = 'draftingAtny'
lawSchool = 'lawSchool'
issueStat = 'issueStat'





#####################insert parsing regulatory info #######################

##############******************************************************
