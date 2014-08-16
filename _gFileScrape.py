# coding: utf-8
import nltk
import re

#******open files (list of files)
with open ('US_7469381_B2_fulltext.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read()
raw = nltk.clean_html(text)

#******scrape data


#******create and write to one new file listing all pubNums and assignees

f = open("googleScrapeInfo.txt","a") #opens file with name of "test.txt"
f.write("and can I get some pickles on that")
f.close()