def insertionSort(l1):
    for i in range(1,len(l1)):
        for j in range(i-1,-1,-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
            else:
                break
    return l1

l2=insertionSort([7,3,8,1,2,0])
print l2

'''def insertionSort(l1):
    for i in range(1,len(l1)):
        j=i-1
        while l1[j]>l1[j+1] and j>=0:
            l1[j],l1[j+1]=l1[j+1],l1[j]
            j-=1
    return l1

print insertionSort([5,4,3,7,2,1])'''
