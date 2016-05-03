#Summing the digits of the number

def digit_sum(num):
    ans=0

    for n in range(len(num)):
        ans=ans+int(num[n])
    return ans 
while True:
    number=raw_input("Enter a number")
    if number=="done":
        break
    if len(number) < 1:
        break
    try:
        num=int(number)
    except:
        print "Enter valid number"
        continue
    print digit_sum(number)
