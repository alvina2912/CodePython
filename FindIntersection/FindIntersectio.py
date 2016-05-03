def findIntersection(A,B):
    c=[]
    for i in A:
        if i in c:
            None
        if i in B:
            c.append(i)
    return c

print findIntersection([1,2,3,4,5,6,7],[3,4,5,6])
