def result1(a):
    s={}
    #a=a.strip(" ")
    result = ""
    for i in range(len(a)):
        if a[i]==" " :
            continue
        if a[i] not in s:
            s[a[i]]=""
            result = result + a[i] + " "
    return result

print result1("aa aa b b b c c")
