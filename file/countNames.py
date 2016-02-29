name=raw_input("Enter the name of the file ")

def countName(name):
    f=open(name)
    count={}
    list=[]
    for line in f:
        line=line.rstrip()
        word=line.split()
        print word
        count[word]=count.get(word,0)+1
    print count
        
    for k,v in count.items():
        list.append((k,v))
    print list
                
countName(name)