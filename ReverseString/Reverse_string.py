# Reverse a String

st=raw_input("Enter a string :")
if len(st)<1:
    print"Enter proper string"
else:
    i=0
    j=len(st)-1
    li=list(st)
    while(i<j):
        temp=li[i]
        li[i]=li[j]
        li[j]=temp
        i+=1
        j-=1
        
print "".join(li)
      
    
#Can be done by storing the sting in another empty string
"""else:
    result=""
    count=len(st)-1
    while count>=0:
        result=result + st[count]
        count=count-1
print result  """
    