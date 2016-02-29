import urllib
import json

url=urllib.urlopen('  http://python-data.dr-chuck.net/comments_239436.json ')
data=url.read()
js=json.loads(data)
print "Retriving ",len(data)," characters"
sum=0
count=0
for item in js['comments']:
    sum+=item['count']
    count=count+1
print "Count :",count
print "Sum : ", sum