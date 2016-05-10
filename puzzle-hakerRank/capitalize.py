ef capi(s):
    l1=s.split()

    for i in range(len(l1)) :
        s = s.replace(l1[i] , l1[i].capitalize())
    return s

print capi(raw_input())
