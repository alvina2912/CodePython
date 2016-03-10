from itertools import product

li=map(int,(raw_input().split()))
li1=map(int,(raw_input().split()))
print list(product(li,li1))

for i in list(product(li,li1)): print i,
