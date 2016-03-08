n=raw_input("Number of element of Set :")
s=set(raw_input("Enter sets element :").split())
N=int(raw_input("Number of operations:"))
for i in range(N):
    operation=raw_input("Operation ").split()
    s1=set(raw_input("Elements of set 2 : ").split())
    if operation[0]=='intersection_update':
        s.intersection_update(s1)
        print s
    elif operation[0]=='update' :
        s.update(s1)
        print s
    elif operation[0]=='symmetric_difference_update':
        s.symmetric_difference_update(s1)
        print s
    elif operation[0]=='difference_update':
        s.difference_update(s1)
        print s
print sum(map(int,s))   