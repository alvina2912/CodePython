students=int(raw_input("Enter number of Students: "))
marksheet=[]
for i in range(students):
    marksheet.append([raw_input(), float(raw_input())])
print marksheet

m=min(item[1] for item in marksheet)
print m

marksheet.sort(key=lambda x: x[1])
print marksheet
li=[]
li=marksheet[1]   
li1=[]
num=li[1]
for item in marksheet:
    if item[1]==num:
         li1.append(item[0])
li1.sort() 
for item in li
    print item
           
