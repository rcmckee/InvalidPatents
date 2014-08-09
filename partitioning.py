import re
#partition creations 3 tuples. 1 of string before the separator, the separator, the string after the separator
your_text = '0000AAA1234ZZZ5678QQQ9123BBB'
infoToPrint = your_text.partition("AAA")[2].partition("ZZZ")[0]   #from http://goo.gl/zatURm
#info partitions at AAA and returns the 3rd-tuple which is the string after AAA. Then we partition the 3rd-turple at the end point ZZZ and return the segment before ZZZ the first turple, which is now just the info between AAA and ZZZ
#if the separator is not there it just returns the entire string in the first turple [0]. So how do I accomodate for this (espectially in Assistant Examiner)?
print infoToPrint





#testing some ideas
text = '000aaa111bbb222ccc333ddd444'
firstPart = text.partition('aaa')[2]
infoArray = firstPart.partition('bbb')
print infoArray[0]

thirdpart = infoArray[2].partition('ccc')
print thirdpart[0]

#creating loop for claims
int_spec = abst[2].partition('1]')
spec = int_spec[2].partition('Claims')
print spec[0]
claim1 = spec[2].partition('2.')
print claim1[0]
claim2 = claim1[2].partition('3.')#if no more claims it will just use the last string so I'm still good as long as I keep using [0] as the last output
print claim1[1]+claim2[0]



