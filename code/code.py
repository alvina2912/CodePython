def getIndex(arr):
    num=0
    if arr==[]:
        return
    num=max(arr)
    answer=arr.index(num)

    return answer

print getIndex([-1,0,5,1,5,3,4,3])
