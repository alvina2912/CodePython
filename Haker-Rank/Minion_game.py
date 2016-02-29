s=raw_input().upper()
#print s
li=[]
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        st=s[i:j]
        li.append(st)
        #print s[i:j]
        
print li
count1=0
count=0
for i in li:
    if i[0] in "AEIOU":  
        print "Kevin : " ,i
        count=count+1
    else :
        print "Stuart : ",i    
        count1+=1
print "Kevins's Points : " ,count
print "Stuart's Points : ",count1

if count>count1:
    print "Kevin ",count
else :
    print "Stuart ", count1