n = input("How many element do u want in set?   ")
s = set(map(int, raw_input("Enter Sets element : ").split())) 
N=input("Enter Number of Operations : ")
for i in range(N):
    operation=raw_input("Operation ").split()
    print operation
    if operation[0]=='pop':
        s.pop()
    elif operation[0]=='remove':   
        s.remove(int(operation[1]))
    elif operation[0]=='discard':   
        s.discard(int(operation[1]))

print s
print sum(s)