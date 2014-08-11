#import mechanize
from urllib import FancyURLopener
#http://wolfprojects.altervista.org/changeua.php
#allows me to get around the error when requesting google. It doesn't like the python user-agent. so change it.

class MyOpener(FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

myopener = MyOpener()
page = myopener.open('https://www.google.com/patents/US5816918')
info = page.read()
print info
#def viewPage(url):
#  browser = mechanize.Browser()
#  page = browser.open(url)
#  source_code = page.read()
#  print source_code

#viewPage('https://www.google.com/patents/US5816918')

