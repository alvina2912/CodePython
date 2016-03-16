pyg = 'ay'
#Input string from user
original = raw_input('Enter a word:')
#check the string is not empty
if len(original) > 0 and original.isalpha():
    word=original.lower()
    first=word[0]
    new_word=word+first+pyg
    new_word=new_word[1:len(new_word)]
    print "Pig Latin Translator : ",new_word
else:
    print 'empty'
