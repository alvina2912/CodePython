# Guessing Game: 2
import random
num=int(raw_input("Enter your number : "))
program_guess=random.randint(0,100)
#print program_guess
count=0
count1=0
while True:
    print program_guess
    if program_guess==num:
        print "Bravo...! Perfect Guess"
        break
    elif program_guess>num:
        print "Kepp guess..! Its bigger Number then user number" 
        program_guess=random.randint(0,program_guess)
        count=count+1
        continue
    else  :
        print "Keep Guessing...! Its smaller Number then user number"
        program_guess=random.randint(program_guess,100)
        count1=count1+1
        continue
print "Guessing happen in ",count1+count," times"
           