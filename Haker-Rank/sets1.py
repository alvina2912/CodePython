n=raw_input()
height=map(int,(raw_input().split()))
print height
height=set(height)
print height
print sum(height)
print len(height)
avg=float(sum(height))/len(height)
print avg