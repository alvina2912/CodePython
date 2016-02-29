m=int(raw_input())
set1=raw_input()
l1=set1.split()
s1=map(int,l1)
n=int(raw_input())
set2=raw_input()
l2=set2.split()
s2=map(int,l2)
s1.sort()
s2.sort()

print "set1 : ", s1
print "set2 : ", s2
l3=[]
for item in s1: 
    if item not in s2:
        l3.append(item)
for item in s2: 
    if item not in s1:
        l3.append(item)       
        
l3.sort()
for item in l3:
    print item