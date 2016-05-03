def anagram(s1,s2):
    if s1==None or s1=="" or s2==None or s2=="":
        return False
    if len(s1)!=len(s2):
        return False
    else:
        r1=sorted(s1)
        r2=sorted(s2)
        if r1==r2:
            return True
        else:
            return False

print anagram("addb","aabd")
