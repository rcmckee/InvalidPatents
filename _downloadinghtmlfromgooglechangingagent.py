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
html = page.read()

file_name = '/Users/robertmckee/Tresors/Projects/InvalidPatents/1stFileGoogle/' + str((numpat.strip()) + '_google.html') # I finally prevented the new line between numpat and '_google.html' by putting numpat.strip() in parenthasis (numpat.strip(). )here I couldn't use the website address because the dashes and the comma after numpat prevents the creation of a new line in the file name which doesn't work either
                  #putting the above path in creates the file name with the path to where it should be made. when put into the newfile = open() function below it will create the new file in that folder which is a different directory/folder than the current script is in. If I didn't add this then the files would just be created in the same folder/directory that this script is in.
print 'file created: ', file_name
newfile = open(file_name,'w') #YAY! saving it as an html file works like a charm motha fucka!
newfile.write(html)
newfile.close()  #When you’re done with a file, call f.close() to close it and free up any system resources taken up by the open file. After calling f.close(), attempts to use the file object will automatically fail.
