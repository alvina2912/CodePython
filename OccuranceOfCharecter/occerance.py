#How to count occurrence of a given character in a String?
def occurrence(s1,s2):
    num=0
    for i in s1:
        if i==s2:
            num+=1
    return num

print occurrence("mary had a little lamb","a")
