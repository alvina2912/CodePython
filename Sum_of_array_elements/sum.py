#The first line of input consists of an integer N. The next line contains N space-separated integers representing the array elements. 
#Sample:

#6
#1 2 3 4 10 11
#Output 
#Output a single value equal to the sum of the elements in the array. 
#For the sample above you would just print 31 since 1+2+3+4+10+11=31.


n=int(raw_input("Enter how many element :"))

sum=0
a=[]
input = raw_input().split(" ")
a=map(int,input) # convert the array of string in array of integer


for i in range (n):
    sum=sum+a[i]
print "Sum = ",sum
