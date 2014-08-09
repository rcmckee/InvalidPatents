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