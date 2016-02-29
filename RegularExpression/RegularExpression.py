#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

import re
handle=open("actual.txt")
result=0
numList=[]
for line in handle:
    line=line.rstrip()
    count=re.findall('[0-9]+',line)
    
    if len(count)>0:
        print count
        for i in map(int,count):
            result=result+i
print "sum= :",result       
       
 
    
    