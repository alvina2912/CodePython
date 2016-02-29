# Find the number is Prime or not
def isPrime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else :
        for n in range(2,num-1):
            if num%n==0:
                return False
        return True
                
    
    
while True: 
    number=raw_input("Enter Numenr : ")

    if number=="done":
        break
    if len(number)<1:
        break
    try:
        num=int(number)
    except:
        print "Enter valid number:"
        continue
    result=isPrime(num)
    if result==True:
        print"The number is Prime"  
    if result==False:
        print "The number is not prime"             
    