# Fibonacci
num=int(raw_input("Enter a number to find Fibonacci sequence :"))

a,b=0,1
for i in range (num):
    print a,
    a,b=b,a+b
