#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

num=int(raw_input("Enter the number to find its all divisers :")
for i in range(1,num):
    if num%i==0:
        print i