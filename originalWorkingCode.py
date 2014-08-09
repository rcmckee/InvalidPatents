import re

with open ('testFullText.rtf', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read() #http://goo.gl/7osxn6 got this code from this thread


primEx = re.search('Primary Examiner</i>&nbsp;&mdash;(.+?)</td>', text) # got this from http://goo.gl/tNMAS3
atnyAgntFirm = re.search('Attorney, Agent, or Firm</i>&nbsp;&mdash;&nbsp;(.+?)</td>', text)

if primEx:
	found_primEx = primEx.group(1)  #http://goo.gl/7osxn6 got this code from this thread
	print found_primEx

if atnyAgntFirm:
	found_atnyAgntFirm = atnyAgntFirm.group(1)
	print found_atnyAgntFirm