# Enter your code here. Read input from STDIN. Print output to STDOUT
#omg lol you guys check thsi thread lmao! legit top lel right there bahah look at the guys face oh man lol

def getoutput(s):
    l1=s.split(" ")
    result=0
    lol,rofl,lmao,lel=1,2,3,4
    for i in range (len(l1)-1):
        if l1[i]=="lol":
            result=result+lol
        elif l1[i]=="rofl":
            result+=rofl
        elif l1[i]=="lmao":
            result+=lmao
        elif l1[i]=="lel":
            result+=lel
        else:
            continue
    if result in range(1,5):
        print "Patient has bright red face"
    if result>=6 and result<=12:
        print "Patient is unable to speak"
    if result>=13 and result<=20:
        print "Patient's sides are mildly bruised"
    if result>=21 and result<=30:
        print "Patient has broken jaw, fractured ribs"
    if result>=31 and result<=49:
        print "Patient is in a coma"
    if result>=50 :
        print "Patient is dead"

getoutput(raw_input())
