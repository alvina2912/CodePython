#l1=[1,2,3,4]
#l2=[2,3,4,5]
#Output : l3=[1,2,2,3,3,4,5]

def sortList(l1,l2):
    l3=[]
    j=0
    k=0
    n=len(l1)+len(l2)
    for i in range(n):
        if j<len(l1) and k < len(l2):
            if l1[j] <= l2[k]:
                l3.append(l1[j])
                j+=1
            else:
                l3.append(l2[k])
                k+=1
        elif j<len(l1):
            l3.append(l1[j])
            j+=1
        else:
            l3.append(l2[k])
            k+=1
    return l3

print sortList([1,2,3,4],[2,3,4,5])
