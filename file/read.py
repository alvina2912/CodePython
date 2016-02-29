#Read a file
import re
f=open("fun.txt",'r')
count=0
total=0
for line in f:
    line=line.strip()
    count+=1
    word=line.split()
    print word
    
    sum=re.findall('[0-9]+',line)
   
    
    for i in map(int,sum):
        total=total+i
print "Tere are %d lines" %count
print "Sum of Numbers:",total

