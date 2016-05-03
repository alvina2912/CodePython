def palindrom(s):
    if s==None or s=="":
        return

    j=len(s)-1
    i=0
    while i < j :
        if s[i]==" ":
            i+=1
            continue
        if s[j]== " " :
            j-=1
            continue
        if s[i]==s[j]:
            j-=1
            i+=1
            return True
        else:
            return True
print palindrom("madam")
