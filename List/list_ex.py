#Take a list, say for example this one:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

li=[2,4,10,6,9,5,10,3,10]
result=[]
for i in li:
    if i<5:
         result.append(i)
print result         
         