#############this works but it creates file names with 2 lines

# coding: utf-8
import nltk
from urllib import urlopen
#to get this to work I need to copy the cells from the excel-->paste into a new textedit file-->select all-->select formart-->make plain text-->save as .txt file-->run program
input_file = open('testUrlList.txt', 'r')
count_lines = 0
for line in input_file:
    print 'from text file ', line, #the comma prevents a new line created. if a new line is created it also creates a '\n' which we don't want if we are using the text for a file name. While it might not show up when printing it will damn sure show up in a file name and fuck up everything. The '\n' tells the computer to look for a file in a new directory so it goes hay wire.
    numpat = str(line) #To write something other than a string, it needs to be converted to a string first with str()
    numpat.strip() #'.strip()' removes the \n 'new line' code that would otherwise print out a bad url with the '\n' and if you have an '\' in the file name it starts looking for a directory so it causes a problem.
    website = str('http://www.google.com/patents/us'+ numpat) #does the comma prevent '\n' from being created?
    print 'website: ', website,
    count_lines += 1
#    html = urlopen(website).read() # to input string variable look at https://stackoverflow.com/questions/17385028/how-to-add-variable-to-url-paramater-in-urllib
    numpat.rstrip()
    file_name = numpat + '_google.html' #here I couldn't use the website address because the dashes and the comma after numpat prevents the creation of a new line in the file name which doesn't work either
    print 'file created: ', file_name
    newfile = open(file_name,'w') #YAY! saving it as an html file works like a charm motha fucka!
#    newfile.write(html)
    newfile.close()  #When you’re done with a file, call f.close() to close it and free up any system resources taken up by the open file. After calling f.close(), attempts to use the file object will automatically fail.
print 'number of lines:', count_lines


#https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
#url = "http://www.lens.org/lens/patent/US_7469381_B2/fulltext"
#do a partition hear to create the file name



#raw = nltk.clean_html(html)  #this code processes the file into text the rest of the code can read. It will need to be in the other files.
#print(raw)