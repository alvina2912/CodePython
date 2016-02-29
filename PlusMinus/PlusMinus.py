#PlusMinus
#Given an array of integers, calculate which fraction of the elements are positive, negative, and zeroes, respectively. 
#Print the decimal value of each fraction.

n=int(raw_input("Enter the limit"))
li=[]
for i in range(n):
    num=raw_input()
    li.append(num)

count=0
count1=0
count2=0
li=map(int, li)
for i in li:
    if i==0:
        count+=1
    elif i>0:
        count1+=1
    elif i<0:
        count2+=1  
           

print li

print count1,round(float(count1)/n,6)
print count2,round(float(count2)/n,6)
print count,round(float(count)/n,6)

