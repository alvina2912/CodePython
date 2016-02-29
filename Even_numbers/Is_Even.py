# Even Numbers
def is_even(num):
    if num % 2==0:
        return True
    else:
        return False   
while True:
    num=raw_input("Enter a number:")
    if len(num)<1:
        break
    if num=="done":
        break    
    try:    
        number=int(num)
    except:
        print "Enter valid number" 
        continue    
    ans=is_even(number)
    if ans==True:
        print "Given Number is Even"
    else:
        print "Given number is Odd"    