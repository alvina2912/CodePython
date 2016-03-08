num=map(int,raw_input().split())
arr=set(map(int,raw_input().split()))
a=set(map(int,raw_input().split()))
b=set(map(int,raw_input().split()))

print num
print arr
print a
print b
happy=0

print arr.intersection(a)
print arr.intersection(b)
print len(arr.intersection(a)) 
print len(arr.intersection(b))
print len(arr.intersection(a))-len(arr.intersection(b))

'''for item in range(len(a)):
    if a[item] in arr:
        happy+=1
    if b[item] in arr:
        happy-=1
print happy '''    
