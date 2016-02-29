#Factorial of a number
def fact(num):
    f=1
    while num>0:
        f=f*num
        num=num-1
    return f   
while True:
    number=raw_input("Enter a number")

    if number=="done":
        break
    if len(number)<1:
        break
    try:
        num=int(number)
    except:
        print "Enter valid number"
        continue
    ans=fact(num)
    print "factorial of %s is" %num,ans