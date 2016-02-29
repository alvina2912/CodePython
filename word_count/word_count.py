#Count how many times the word present in a list
def count(list_of_words, word):
    c=0
    
    for i in list_of_words :
        
        if word==i:
            c=c+1
    return c
     
#print count(['abc','abc','abc','aaa', 'abc'],'abc') 

bigString=raw_input("Enter sentence: ")  
smallString=raw_input("Enter the word to search in the sentence :")
li=[]
li=bigString.split() 
print count(li,smallString)