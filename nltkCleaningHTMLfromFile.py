import nltk   

#https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
#I could do a loop for a url list example https://stackoverflow.com/questions/18952351/scrape-html-files-stored-in-remote-directory
#with open ('lens-patent-US7469381B2-fulltext.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
	#text=myfile.read() 

with open ('htmlonlyview-source www.lens.org lens patent US_7469381_B2 fulltext.html', "r") as myfile:   #http://goo.gl/7osxn6 got this code from this thread
    text=myfile.read()   #need to use a file that is downloaded as a complete webpage not the html only option
raw = nltk.clean_html(text)  
print(raw)
#shit this is clean



