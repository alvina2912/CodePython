import urllib

f=urllib.urlopen('http://www.marieclaire.com/beauty/hair/how-to/g2614/10-easy-quick-hairstyles-in-10-seconds/')
for line in f:
    print line