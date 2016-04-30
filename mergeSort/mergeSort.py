def marge(l1,start,middle,end):
    left=l1[start:middle+1]
    right=l1[middle+1:end+1]
    j=0
    k=0
    for i in range(start,end+1,1):
        if j<len(left) and k <len(right):
            if left[j] <= right[k]:
                l1[i]=left[j]
                j+=1
            else:
                l1[i]=right[k]
                k+=1
        elif j<len(left):
            l1[i]=left[j]
            j+=1
        elif k< len(right):
            l1[i]=right[k]
            k+=1

def mergeSort(l1,first,last):
    if l1==None or len(l1)==0 :
        return
    if first >=last:
        return

    middle=(first+last)/2
    mergeSort(l1,first,middle)
    mergeSort(l1,middle+1,last)
    marge(l1,first,middle,last)
    return l1


l1=[5,4,6,8,2,9,10]
print "Give List",l1
l2=mergeSort(l1,0,len(l1)-1)
print "Sorted List",l2
