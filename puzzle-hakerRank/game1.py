n=int(raw_input())
li=raw_input()
bLevel=map(int,li.split())
h=10
level=1
bugcount=0

for i in range(len(bLevel)):
    if bLevel[i]==level:
        h-=bLevel[i]
    if bLevel[i]>level:
        h-=(2*bLevel[i])
    if bLevel[i]<level:
        h-=1

    if h<=0:
        print "You have died. Reached level %d and killed %d bugs" %(level,bugcount)
        break
    bugcount+=1
    if bugcount%3==0:
        h=15
        level+=1
