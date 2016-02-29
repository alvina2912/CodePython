# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

def palindrome(word):
    j=len(word)-1
    i=0
    while(i<j):
        if word[i]==word[j]:
            return True
        else :
           return False
        i+=1
        j-=1   
        
word=raw_input("enter a word : ")
result=palindrome(word)
if result==True:
    print "Given word is Palindrome"
else:
    print"Given word is not a Palindrome"    