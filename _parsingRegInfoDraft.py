# coding: utf-8
import nltk
import re

#####################parsing regulatory info #######################
#files to test
#htmlonlyviewUS_7469381_B2 regulatory.html
#htmlonlyviewUS_5612524_A regulatory.html


with open ('htmlonlyviewUS_5612524_A regulatory.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read()   #need to use a file that is downloaded as a complete webpage not the html only option
raw = nltk.clean_html(text)

#have regInfo but only if claims are canceled. List those claims. find 'ARE CANCELLED.' (make it in any case) then go back from that and look for '.' how do I go bavk in a partition?
#this will need to be a loop of some sort to check for multiple reexaminations
cancelledClaimsSearch = re.search('CANCELLED', raw, re.IGNORECASE)
regInfo = raw
if cancelledClaimsSearch == False: #if the re.search function doesn't finds 'cancelled' then I want it to partition that area out.
  print 'not cancelled'

#use re.search each time to look more for cancelled. that will tell you if you need to keep going.
#if cancelled then look for
else:
  int_regInfo = raw.partition('REEXAMINATION CERTIFICATE') #partition so I can limit what I have to search
  if re.search('confirmed', int_regInfo[2], re.IGNORECASE) == False: # if it doesn't find confirmed then this is the part that has cancelled. there might be another one but I will get to that later
    regInfo = int_regInfo[2].partition('CANCELLED')
    print int_regInfo[1]+' '+ regInfo[0] + regInfo[1]
    if re.search('CANCELLED', regInfo[2], re.IGNORECASE) == False:
      print 'there is no other cancelation event'
    else:
      print 'there is another cancelation event'
  else:      #what to do if confirmed is found. if I find confirmed then I would partition at it then look for cancelled. then test for another cancelled. for now just say
    regInfoCnfrmd = int_regInfo[2].partition('CONFIRMED') #we have found 'CONFIRMED' now we can look for cancelled.
    regInfoCncld = regInfoCnfrmd[2].partition('CANCELLED') #we habe found cancelled. now we can print out what we have found.
    regInfo = regInfoCnfrmd[0] + regInfoCnfrmd[1] +' '+ regInfoCncld[0] + regInfoCncld[1]+'.' #this is putting together all the strings/tuples (is it tuples? fuck it.)
    print regInfo + '*********does this print?**********'
    #this leaves in a lot of stuff
#THIS ISN'T FUCKING WORKING  if re.search('CANCELLED', regInfoCncld[2], re.IGNORECASE) == False:
#    print 'no mas $$$$$$$$$$$$$$$'
#  else:
#    print 'another one$$$$$$$$$$$$$$$$$$$$$$'
  # check to see if another cancelled is found. Would a while loop work here?


#
#  regInfo = int_regInfo[2].partition('CANCELLED')
#need to have a check to see if the first one is the only one. first one have check for FIRST REEXAMINATION, THEN CHECK FOR A SECOND REEXAMINATION FROM THAT PARTITIONED STRING. THEN HAVE IF ELSE CODES
#  if re.search('CANCELLED', regInfo[2], re.IGNORECASE)
#  print regInfo[0] + regInfo[1]

#will need loop to check for another cancelled

#currently it finds the first reexamination then prints everything out after confirmed.



