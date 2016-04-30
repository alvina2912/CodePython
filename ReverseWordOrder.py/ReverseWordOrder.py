#Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.

'''def reverseWord(s):
    li=[]
    li=s.split()
    #print li
    for i in reversed(li):
        print i,'''

def reverseWord(s):
    s=s.split()
    l=len(s)-1
    while l>=0:
        print "".join(s[l]),
        l-=1



reverseWord("my name is alvina and i like python")
