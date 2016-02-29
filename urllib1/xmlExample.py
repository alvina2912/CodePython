import urllib
import xml.etree.ElementTree as ET

url=urllib.urlopen('http://python-data.dr-chuck.net/comments_239432.xml')

data=url.read()
tree=ET.fromstring(data)

count=tree.findall('comments/comment')
sum=0
for item in count:
    num=int(item.find('count').text)
    sum+=num

print sum