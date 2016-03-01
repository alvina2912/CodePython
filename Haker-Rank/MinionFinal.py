s=raw_input().upper()
stourtCount=0
kevinCount=0
for i in range(len(s)):
    if s[i] in "AEIOU":
        stourtCount+=len(s)-i
    else:
        kevinCount+=len(s)-i
if stourtCount == kevinCount :
    print "Draw"
elif  stourtCount > kevinCount :
    print "Srourt",stourtCount
else :
    print "Kevin",kevinCount               
