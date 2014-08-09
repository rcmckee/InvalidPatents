#https://docs.python.org/2.7/library/fileinput.html
#file_input = testUrlList.txt

#import fileinput
#for line in fileinput.input(testUrlList.txt):
#    process(line)
#    print line

#https://stackoverflow.com/questions/19140375/python-how-to-loop-through-a-text-file-of-urls-and-pass-all-the-urls-into-a-re
#filename = testUrlList.txt
#def get_lots_of_urls(filename):
#    with open(filename) as infile:
#        return [get_redirect_url(url.strip()) for url in infile]

#for redirect_url in get_lots_of_urls('testUrlList.txt'):
#    print redirct_url

#https://stackoverflow.com/questions/11726349/python-looping-through-input-file
input_file = open('testUrlList.txt', 'r')
count_lines = 0
for line in input_file:
    print line
    count_lines += 1
print 'number of lines:', count_lines
