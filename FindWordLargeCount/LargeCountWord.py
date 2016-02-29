#Find the word from the file whose count it larger

name=raw_input("Enter name of the file : ")

handle=open(name,'r')
text=handle.read()
words=text.split()

counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
print counts.items()

for word,count in counts.items():
    if bigcount is None or count>bigcount :
        bigword=word
        bigcount=count
print bigword, bigcount
        