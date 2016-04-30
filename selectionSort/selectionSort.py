def selectionSort(l1):
    for i in range(len(l1)-1):
        minIndex=i
        for j in range(i+1,len(l1)):
            if l1[j]<l1[minIndex]:
                minIndex=j
        if minIndex !=i:
            l1[i],l1[minIndex]=l1[minIndex],l1[i]
    return l1

l2=selectionSort([6,5,4,7,3,2,8,1])
print l2
