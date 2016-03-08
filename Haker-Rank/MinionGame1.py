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
if count > count1:
    print "Stuart :",count
else :    
    print "Kevin :",count1            
        


        

