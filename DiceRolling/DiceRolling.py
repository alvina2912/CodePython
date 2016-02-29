#Dice Rolling Simulator:
from random import randint
print"Lets Play Dice Rolling"
play_more='y'
while play_more=='y':
    user_guess=int(raw_input("Guess the number :"))
    if user_guess<1 or user_guess>6:
        print"Enter the proper number bertween 1-6:"
        continue
    minNum=1
    maxNum=6    
    dice=randint(minNum,maxNum)
    print "Dice number:" ,dice
    if user_guess==dice:
        print "U guess the right number"
        play_more=raw_input("Do you wanna play more(Y/N)?").lower()
        if play_more=='y':
            continue
        else:
            break    
    else:
        if dice>user_guess:
            diff=dice-user_guess
            print "Wrong Guess, Too Low..!! u have lost by %d points"%diff
        else:
            diff=user_guess-dice
            print "Wrong Guess,Too High...!! u have lost by %d points"%diff    
        play_more=raw_input("Do you wanna play more(Y/N)?")
        if play_more=='y':
            continue
        else:
            break    
           
