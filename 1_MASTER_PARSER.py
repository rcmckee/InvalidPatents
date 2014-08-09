# coding: utf-8
import nltk
import re
import sqlite3

#******************ANONYMOUS BROWSER*****************



#******************SCRAPE FULL TEXT******************

with open ('2ndtestpageview-source www.lens.org lens patent US_5612524_A fulltext.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read()
raw = nltk.clean_html(text)


int_pubNum = raw.partition(' - ')
pubNum = int_pubNum[0]
print pubNum+'test to see if printing pubNum'
title = int_pubNum[2].partition(' - \nThe Lens') #had to put in the \n for new line. otherwise it didn't recognize it and just returned the entire string. lets see how specific that is on other documents.
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

int_primEx = fieldSrch[2].partition('Primary Examiner') #2nd test, primary examiner prints out
primExAsEx = int_primEx[2].partition('Assistant Examiner')
s_primExAsEx = primExAsEx[2]
primEx = primExAsEx[2]#make this so that the following else statement has a value to change  to change if no 'Assistant Examiner' is found
assEx = ' '
if len(s_primExAsEx) > 1:
  print int_primEx[1]+' '+primExAsEx[0] + 'test to see if this is actually printing out int_primEx if "Assistant Examiner" is found'
  primEx = int_primEx[1]+ ' '+primExAsEx[0] # test to see if uploading primEx to db when assistant examiner is found
  assEx = primExAsEx[2].partition('Art Unit')
  print  primExAsEx[1]+assEx[0]+' test to see if printing assEx[0] when "Assistant Examiner" is found'
  assEx = primExAsEx[1]+assEx[0] #new hopefully uploads the assistant examiner into the database

else:
  primExAU = int_primEx[2].partition('Art Unit')
  print primExAU[0]+' test to see if printing primExAU[0] when "Assistant Examiner" is not found'
  primEx = primExAU[0] #i changed this from primExAu[2]. I didn't want that put into the db.

int_atnyAgntFirm = int_primEx[2].partition('Attorney, Agent, or Firm') #changed this from partitioning primEx
s_int_atnyAgntFirm = int_atnyAgntFirm[2]
atnyAgntFirm = int_atnyAgntFirm[0]
if len(s_int_atnyAgntFirm) > 1:                       #this means it found attorney agent firm; which it will do in most cases
  atnyAgntFirm = s_int_atnyAgntFirm.partition('(5')   #
  print atnyAgntFirm[0]+'test to see if printing atnyAgntFirm[0]'
  atnyAgntFirm = atnyAgntFirm[0]        #changed from atnyagntfirm[2] to [0] then changed the later code to referense
else:
  atnyAgntFirm = 'none'


int_abst = int_primEx[2].partition('7)') #goes from primary examiner to abstract regardless of if atnyAgntFirm is found or not
abst = int_abst[2].partition('Draw')
print abst[0]+'test to see if printing abst'
int_spec = abst[2].partition('ng')
spec = int_spec[2].partition(' (57)')
#print spec[0]+'test to see if printing spec'
print spec[1] +"just during test to see if spec is printing but so I don't have to scroll up through the entire spec"
claim1 = spec[2].partition('2.')
print claim1[0]+'test to see if printing claim1'
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
##############################*VARIABLES FOR DATABASE*#################################
title = title[0]
patNum = patNum[0]
inventors = inventors[0]
assgnee = assgnee[0]
filingDat = filingDat[0]
intlClass = intlClass[0]
usaClass = usaClass[0]
fieldSrch = fieldSrch[0]
#primEx should be accounted for since I had to define it for the if statment to have a variable to change
#assEx should be accounted for since I had to define it for the if statment to have a variable to change
#atnyAgntFirm should be accounted for since I had to define it for the if statment to have a variable to change
abst = abst[0]
spec = spec[0]  #just keep as a comment so it is easy to look through in terminal while testing
dbclaim1 = claim1[0]
dbclaim2 = claim1[1]+claim2[0]
dbclaim3 = claim2[1]+claim3[0]
dbclaim4 = claim3[1]+claim4[0]
dbclaim5 = claim4[1]+claim5[0]
dbclaim6 = claim5[1]+claim6[0]
dbclaim7 = claim6[1]+claim7[0]
dbclaim8 = claim7[1]+claim8[0]
dbclaim9 = claim8[1]+claim9[0]
dbclaim10 = claim9[1]+claim10[0]
dbclaim11 = claim10[1]+claim11[0]
dbclaim12 = claim11[1]+claim12[0]
dbclaim13 = claim12[1]+claim13[0]
dbclaim14 = claim13[1]+claim14[0]
dbclaim15 = claim14[1]+claim15[0]
dbclaim16 = claim15[1]+claim16[0]
dbclaim17 = claim16[1]+claim17[0]
dbclaim18 = claim17[1]+claim18[0]
dbclaim19 = claim18[1]+claim19[0]
dbclaim20 = claim19[1]+claim20[0]



draftingAtny = 'draftingAtny'
lawSchool = 'lawSchool'
issueStat = 'issueStat'

#******************SCRAPE REGULATORY INFO************

with open ('htmlonlyviewUS_7469381_B2 regulatory.html', "r") as myfile:
    text=myfile.read()
raw = nltk.clean_html(text)

cancelledClaimsSearch = re.search('CANCELLED', raw, re.IGNORECASE)
regInfo = raw
if cancelledClaimsSearch == False:
  print 'not cancelled'

else:
  int_regInfo = raw.partition('REEXAMINATION CERTIFICATE')
  if re.search('confirmed', int_regInfo[2], re.IGNORECASE) == False:
    regInfo = int_regInfo[2].partition('CANCELLED')
    print int_regInfo[1]+' '+ regInfo[0] + regInfo[1]
    if re.search('CANCELLED', regInfo[2], re.IGNORECASE) == False:
      print 'there is no other cancelation event'
    else:
      print 'there is another cancelation event'
  else:
    regInfoCnfrmd = int_regInfo[2].partition('CONFIRMED')
    regInfoCncld = regInfoCnfrmd[2].partition('CANCELLED')
    regInfo = regInfoCnfrmd[0] + regInfoCnfrmd[1] +' '+ regInfoCncld[0] + regInfoCncld[1]+'.'
    print regInfo + '*********does regInfo print?**********'

#******************INSERT INTO DATABASE**************
# to learn how to do this see https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.execute

db = sqlite3.connect('1ipDatabase.sqlite') #need .sqlite extension and maybe open file with sqlite?
db.text_factory = str
cursor = db.cursor()
cursor.execute('insert into patent values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(pubNum, title, patNum, inventors, assgnee, filingDat, intlClass, usaClass, fieldSrch, primEx, assEx, atnyAgntFirm, abst, spec, dbclaim1, dbclaim2, dbclaim3, dbclaim4, dbclaim5, dbclaim6, dbclaim7, dbclaim8, dbclaim9, dbclaim10, dbclaim11, dbclaim12, dbclaim13, dbclaim14, dbclaim15, dbclaim16, dbclaim17, dbclaim18, dbclaim19, dbclaim20, regInfo, draftingAtny, lawSchool, issueStat))
#cursor.execute('select * from patent where pubNum=:pubNum and title=:title and patNum=:patNum and inventors=:inventors and assgnee=:assgnee and filingDat=:filingDat and intlClass=:intlClass and usaClass=:usaClass and fieldSrch=:fieldSrch and primEx=:primEx and assEx=:assEx and atnyAgntFirm=:atnyAgntFirm and abst=:abst and spec=:spec and dbclaim1=:claim1 and dbclaim2=:claim2 and dbclaim3=:claim3 and dbclaim4=:claim4 and dbclaim5=:claim5 and dbclaim6=:claim6 and dbclaim7=:claim7 and dbclaim8=:claim8 and dbclaim9=:claim9 and dbclaim10=:claim10 and dbclaim11=:claim11 and dbclaim12=:claim12 and dbclaim13=:claim13 and dbclaim14=:claim14 and dbclaim15=:claim15 and dbclaim16=:claim16 and dbclaim17=:claim17 and dbclaim18=:claim18 and dbclaim19=:claim19 and dbclaim20=:claim20 and regInfo=:regInfo and draftingAtny=:draftingAtny and lawSchool=:lawSchool and issueStat=:issueStat', {"pubNum":pubNum, "title":title, "patNum":patNum, "inventors":inventors, "assgnee":assgnee, "filingDat":filingDat, "intlClass":intlClass, "usaClass":usaClass, "fieldSrch":fieldSrch, "primEx":primEx, "assEx":assEx, "atnyAgntFirm":atnyAgntFirm, "abst":abst, "spec":spec, "claim1":dbclaim1, "claim2":dbclaim2, "claim3":dbclaim3, "claim4":dbclaim4, "claim5":dbclaim5, "claim6":dbclaim6, "claim7":dbclaim7, "claim8":dbclaim8, "claim9":dbclaim9, "claim10":dbclaim10, "claim11":dbclaim11, "claim12":dbclaim12, "claim13":dbclaim13, "claim14":dbclaim14 , "claim15":dbclaim15, "claim16":dbclaim16, "claim17":dbclaim17, "claim18":dbclaim18, "claim19":dbclaim19, "claim20":dbclaim20, "regInfo":regInfo, "draftingAtny":draftingAtny, "lawSchool":lawSchool, "issueStat":issueStat})

db.commit()
print pubNum+ ' inserted into database.'
#print cursor.fetchone() #long crazy list
db.close()

