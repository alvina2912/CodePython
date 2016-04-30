def bubbleSort(l1):
    for i in range(len(l1)-1):
        for j in range(0,len(l1)-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1

l2=bubbleSort([4,3,4,3,2,9,0])
print l2
