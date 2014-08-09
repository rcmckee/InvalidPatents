
from BeautifulSoup import BeautifulSoup
tree = BeautifulSoup('lens-patent-US7469381B2-fulltext.html')
good_html = tree.prettify()

print good_html