print "** Temrature Converter **"
temp=int(raw_input("Enter Temprature :"))
choice=raw_input("Convert to (F)ahrenheit or (C)elsius?")

def ConvertToC(temp):
    Tf=(float(9)/5)*temp+32
    return Tf

def ConvertToF(temp):
    Tc=(float(5)/9)*(temp-32)
    return Tc

while choice :
    if choice.upper()=='F':
        ans=ConvertToF(temp)
        print temp,"F =",ans,"C"
        break
    elif choice.upper()=='C' :
        ans1=ConvertToC(temp)
        print temp,"C=",ans1,"F"
        break
    else :
        print"Wrong Choice "
        break
