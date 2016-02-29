import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    num=int(tag.string)
    sum+=num
    print 'Num:',num
print "sum = ",sum    
    
    
    