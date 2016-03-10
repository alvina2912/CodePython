from collections import Counter
x=int(raw_input("Enter numner of shoes pairs :"))
ShoeSize=[int(raw_input("Enter Shoe sizes :")) for i in range(x)]
N=int(raw_input("Enter number of customers:"))
li=[]
li1=[]
for i in range(N):
    li.append(map(int,(raw_input("Enter shoe size, price :")).split()))
    #size, price=int(raw_input("enter shoe size, price"))

print x
print ShoeSize
print N
print li
li1=Counter(ShoeSize).items()
print li1
print li1[0][1]
