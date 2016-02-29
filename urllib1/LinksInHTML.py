import urllib
from BeautifulSoup import *
link=raw_input("Enter link :")
html=urllib.urlopen(link).read()
count=int(raw_input("Enter Count : "))
position= int(raw_input("Enter Position : "))

print "URL:" ,link
for i in range(count):
    html=urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    tags = soup.findAll('a')
    link=tags[position-1].get('href', None)
    print 'URL:',link
        
   