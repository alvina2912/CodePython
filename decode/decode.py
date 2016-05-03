# s=(a2d3)
#output= aaddd

def decode(s1):
    result=""
    for i in range (len(s1)-1):
        if i%2 != 0 :
            continue
        else:
            result+=s1[i]*int(s1[i+1])
    return result

def encode(s1):
    result=""
    for i in range (len(s1)-1):
        if s1[i]==s1[i+1]:
            continue
        else:
            num=s1.count(s1[i])
            result+=s1[i]+str(num)
    return result



print decode("a2d3f4")
print encode("aaabbccddd")
