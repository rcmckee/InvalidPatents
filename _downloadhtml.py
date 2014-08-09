import nltk
from urllib import urlopen
#https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
#I could do a loop for a url list example https://stackoverflow.com/questions/18952351/scrape-html-files-stored-in-remote-directory
url = "http://www.lens.org/lens/patent/US_7469381_B2/fulltext"
#do a partition hear to create the file name
html = urlopen(url).read()
newfile = open('US_7469381_B2_fulltext.html','w') #YAY! saving it as an html file works like a charm motha fucka!
newfile.write(html)


raw = nltk.clean_html(html)  #this code processes the file into text the rest of the code can read. It will need to be in the other files.
print(raw)


#shit this is super clean

