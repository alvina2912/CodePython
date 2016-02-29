#File overlaping

f1=open("FileOne.txt")
f2=open("FileTwo.txt")
primeList=[]
happyList=[]
a=f1.readline()
while a:
    primeList.append(int(a))
    a=f1.readline()
b=f2.readline()
while b:
     happyList.append(int(b))  
     b=f2.readline()
   
overlaping=[]
for elem in primeList:
    if elem in happyList:
        overlaping.append(elem)
        

print "PrimeList : ",primeList
print"HappyList : ",happyList
print "Overlaping List : ", overlaping
