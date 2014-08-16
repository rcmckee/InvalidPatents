# coding: utf-8
import nltk
import re
import sqlite3
import string

#******************ANONYMOUS BROWSER*****************



#******************SCRAPE FULL TEXT******************

with open ('2ndtestpageview-source www.lens.org lens patent US_5612524_A fulltext.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read()
raw = nltk.clean_html(text)
filtered_string = ''.join(filter(lambda x:x in string.printable, raw))
print filtered_string