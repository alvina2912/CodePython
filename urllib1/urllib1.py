import urllib
fhand=urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')

for line in fhand:
    line.rstrip()
    word=line.split()
    print word