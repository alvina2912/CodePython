# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

a=[5, 10, 15, 20, 25]
b=[]

def findFirstNLastElement(li):
    num1=li[0]
    num2=li[len(li)-1]
    b.append(num1)
    b.append(num2)
    return b

print findFirstNLastElement(a)
