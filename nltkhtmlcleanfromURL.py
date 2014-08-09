import nltk
from urllib import urlopen
#https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
#I could do a loop for a url list example https://stackoverflow.com/questions/18952351/scrape-html-files-stored-in-remote-directory
url = "http://www.lens.org/lens/patent/US_7469381_B2/fulltext"
html = urlopen(url).read()
raw = nltk.clean_html(html)
print(raw)

#shit this is super clean
