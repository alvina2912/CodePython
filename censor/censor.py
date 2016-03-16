def censor(text, word):
    arrayOfWords=text.split(" ")
    answer=[]
    for tx in arrayOfWords:
        if word==tx:
            t= "*" * len(word)
            answer.append(t)

        else:
            answer.append(tx)


    return " ".join(answer)

text=raw_input("Enter your Sentence : ")
word=raw_input("Enter the word tht you want to cahnge to * : ")
print censor(text,word)
