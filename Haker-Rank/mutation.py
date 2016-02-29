s=raw_input()
li=list(s)
s1=raw_input().split()
print li
print s1
num=int(s1[0])
print num
char=s1[1]
print char
li[num]=char

print "".join(li)
