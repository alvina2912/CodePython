

def substringCount(s,st):
    return s.count(st)  


s=raw_input().upper()
count=0
count1=0
result={}
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        st=s[i:j]
       
        
        if st[0] in "AEIOU":
            print "Stuart : ", st
            a=substringCount(s,st)
            if st in result.keys():
                pass
            else:
                result[st]=a
                count=count+a
                print substringCount(s,st)
            
        else:
            print "Kevin  : ",st
            b=substringCount(s,st)
            if st in result.keys():
                pass
            else:
                result[st]=b
                count1=count1+b
                print substringCount(s,st)     
print result
print "Stuart :",count
print "Kevin :",count1            
        


        

'''print li
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
    print "Stuart ", count1'''