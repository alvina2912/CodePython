f=open("fun.txt","r")
data=f.copy()
f.close()

f1=open("fun1.txt","w")
f1.write(data)
f1.close