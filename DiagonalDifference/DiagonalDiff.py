#Diagonal Difference

n = int(raw_input())
matrix = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    inputArray = raw_input().split(' ')
    for j in range(n):
        matrix[i][j] = int(inputArray[j])
        
        
print(matrix)
sum=0
for i in range(n):
    sum=sum+matrix[i][i]
print "Sum of first Diagonal :", sum

sum1=0
j=n-1
for i in range(n):
    sum1=sum1+matrix[i][j]
    j-=1
print "Sum of second Diagonal:",sum1

print abs(sum-sum1)


    
