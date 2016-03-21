a=[1,1,2,5]
b=[2,5,7]
d={}
result=[]
for i in range(len(a)):
    d[a[i]]="true"
for i in range (len(b)):
    if b[i] in d.keys():
        result.append(b[i])
print result
