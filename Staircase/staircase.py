# Print StairCase with #

n = int(raw_input().strip())

for i in range(n):
    print "#"*i
j=1
  
for i in range(n-1,0,-1):
    print " "*i + "#"*j  
    j+=1  