#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn
# 100 years old.

from datetime import date

name=raw_input("Enter your Name:")
age=int(raw_input("Enter your age :"))
if age<1 and ange>100:
    print"Enter Proper Age"
else:
    result=100-age
     
print "Your Name is %s and your Age is %d"%(name,age)

print "%d years remaning for you to turn 100" %result 

yr=date.today().year+result
print "you will tern 100 on " ,yr
 
        