#Create a program that will play the cows and bulls game with the user. The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
#For every digit that the user guessed correctly in the correct place, they have a cow. 
#For every digit the user guessed correctly in the wrong place is a bull.
#Every time the user makes a guess, tell them how many cows and bulls they have. 
#Once the user guesses the correct number, the game is over.
#Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
rand= random_with_N_digits(4)
rand=str(rand)
print rand
count=0
count1=0
numberOfGuessess=0
while True:
    userInput=raw_input("Enter a Number ")
    print userInput
    
    for i in range(len(rand)):
        if userInput[i]==rand[i]:
            count=count+1
        for j in range(i+1,len(rand)):
            if userInput[i]==rand[j]:
                count1+=1 
    if count!=4:
        print "Cows = ",count
        print "Bulls =" ,count1
        print "Keep Guessing...!"
        numberOfGuessess+=1
        print "num of Guesssing :" ,numberOfGuessess
        continue            
    if count==4 and count1==0:
        print "Congratulations...!! U guess the right number "
        print "you took ",numberOfGuessess," turns to guess the number"
        break
    
                   

