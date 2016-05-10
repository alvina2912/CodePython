def game(numOfBugs,bugLevel):
    buglevel=map(int,bugLevel.split())
    level=1
    health=10
    bugcount=0
    for i in range(numOfBugs):
        if bugcount%3==0:
            health=15
            level+=1


        if buglevel[i]==level:


            if health<=0 and health<buglevel[i]:
                print "You have died. Reached level %d and killed %d bugs" %(level,bugcount)
                break
            health-=buglevel[i]
            bugcount+=1

        elif buglevel[i]>level:

            if health<=0 and health<buglevel[i]:
                print "You have died. Reached level %d and killed %d bugs" %(level,bugcount)
                break
            health-=(2*buglevel[i])
            bugcount+=1
        else:
            health-=1
            if health<=0 and health<buglevel[i]:
                print "You have died. Reached level %d and killed %d bugs" %(level,bugcount)
                break

            bugcount+=1



a=int(raw_input())
b=raw_input()
game(a,b)
