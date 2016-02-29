#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def removeDuplicates(li):
    result=[]
    for i in li:
        if i not in result:
            result.append(i)
    return result       
     
print removeDuplicates([1,1,1,2,2,2,3,3,3,4,4,4,5,5,1,1,1,2,2,2,3])     