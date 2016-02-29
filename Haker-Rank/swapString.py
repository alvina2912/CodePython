s=raw_input()
li=[]
for i in s:
    if i.isupper():
       li.append(i.lower()) 
    else:
       li.append(i.upper())

print "".join(li)