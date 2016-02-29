#Use the BeautifulSoup and requests Python packages to print out a list of all 
#the article titles on the New York Times homepage.

import urllib
from BeautifulSoup import *

url="http://www.nytimes.com/"
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
tags=soup.findAll('article')

for line in tags:
    print line.text ,"\n"

