def reverseString(s):
    temp=""
    j=len(s)-1
    i=0
    while j>i:
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
        j-=1
        i+=1
    return s



s = "abc"
reverseString(s)
print s
