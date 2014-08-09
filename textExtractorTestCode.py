# coding: utf-8
# above is from http://goo.gl/GmR23L
import re

with open ('testFullText.rtf', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read() #http://goo.gl/7osxn6 got this code from this thread

def remove_tags(input_text):
	# convert in_text to a mutable object (e.g. list)
	s_list = list(input_text)
	i,j = 0,0
	while i < len(s_list):
		# iterate until a left-angle bracket is found
		if s_list[i] == '<':
			while s_list[i] != '>':
				# pop everything from the the left-angle bracket until the right-angle bracket
				s_list.pop(i)
			# pops the right-angle bracket, too
			s_list.pop(i)
		else:
			i=i+1
	# convert the list back into text
	join_char=''
	return join_char.join(s_list)
 
#Now just pass an HTML formatted text through this function .It remove the tags and return the string
test_txt = text
st = remove_tags(test_txt)
print st  # it will print "This is HTML text"


pubNum = re.search('<title>(.+?) -', text)
title = re.search('<title>(.+?)</title>', text)
#patNum = re.search('____(.+?)___', text)
issueStat = re.search('<em class="doc-type">(.+?)</em>', text) # ERROR SyntaxError: Non-ASCII character '\xc2' in file textExtractor.py on line 9, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
filingDat = re.search('Filed: </td><td class="table_data"><b>(.+?)</b></td>', text)
intlClass = re.search('Int. Cl.</b></td><td class="separator">&nbsp;</td><td align="right" class="nowrap_text">(.+?)</td>', text)
usaClass = re.search('U.S. Cl.</b></td><td class="separator">&nbsp;</td><td align="right" class="nowrap_text">(.+?)</td>', text)
fieldsrch = re.search('Field of Search </b></td><td class="separator">&nbsp;</td><td align="right" class="nowrap_text">(.+?)</td>', text)
primEx = re.search('Primary Examiner</i>&nbsp;&mdash;(.+?)</td>', text) # got this from http://goo.gl/tNMAS3
#assEx = re.search('____(.+?)___', text)
atnyAgntFirm = re.search('Attorney, Agent, or Firm</i>&nbsp;&mdash;&nbsp;(.+?)</td>', text)
#regInfo = re.search('______(.+?)______', text)
inventors = re.search('Inventor: </td><td class="table_data"><b>(.+?)</td>', text)
assgnee = re.search('Assignee:</td><td class="table_data"><b>(.+?)</td><tdclass="table_data">&nbsp;</td>', text)
abst = re.search('<h2>Abstract</h2></td></tr></table><div class="para_text"><table rules="none" width="95%" border="0"><tr><td valign="top"><div class="para_text">(.+?)</td></tr></table>', text)       #this might require the \n because there are a lot of line breaks in the normal code
#spec = re.search('______(.+?)______', text)
claims = re.search('<h2>Claims</h2></td></tr><tr><td class="para_text" valign="top" colspan="3"><a name="CLM-00001"></a><div class="claim_text">(.+?)</div></td></tr></table></div>', text)     #this might require the \n because there are a lot of line breaks in the normal code
#draftingAtny = re.search('______(.+?)______', text)
#lawSchool = re.search('______(.+?)______', text)

if pubNum:
	found_pubNum = pubNum.group(1)
	print found_pubNum

if title:
	found_title = title.group(1)
	print found_title

#if patNum:
#	found_patNum = patNum.group(1)
#	print found_patNum

if issueStat:
	found_issueStat = issueStat.group(1)
	print found_issueStat

if filingDat:
	found_filingDat = filingDat.group(1)
	print found_filingDat

if intlClass:
	found_intlClass = intlClass.group(1)
	print found_intlClass

if usaClass:
	found_usaClass = usaClass.group(1)
	print found_usaClass

if fieldsrch:
	found_fieldsrch = fieldsrch.group(1)
	print found_fieldsrch


if primEx:
	found_primEx = primEx.group(1)  #http://goo.gl/7osxn6 got this code from this thread
	print found_primEx
#else 
#do an else if statement to check for errors in the find flags like else if 'Primary Examiner' is found print error because if it doesn't find primEx but 'Primary Examiner' is there it means the start and end points I had are wrong	
#this worked but I had to copy the html file text and past it into textedit to make a .rtf file.

#if assEx:
#	found_assEx = assEx.group(1)
#	print found_assEx

if atnyAgntFirm:
	found_atnyAgntFirm = atnyAgntFirm.group(1)
	print found_atnyAgntFirm
#works

#if regInfo:
#	found_regInfo = regInfo.group(1)
#	print found_regInfo

if inventors:
	found_inventors = inventors.group(1)
	print found_inventors

if assgnee:
	found_assgnee = assgnee.group(1)
	print found_assgnee

if abst:
	found_abst = abst.group(1)
	print found_abst

#if spec:
#	found_spec = spec.group(1)
#	print found_spec

if claims:
	found_claims = claims.group(1)
	print found_claims

#if draftingAtny:
#	found_draftingAtny = draftingAtny.group(1)
#	print found_draftingAtny

#if lawSchool:
#	found_lawSchool = lawSchool.group(1)
#	print found_lawSchool