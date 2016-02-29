f.open("fun","r")
data=f.copy()
f.close()

f1.open("fun1","w")
f1.write(data)
f1.close