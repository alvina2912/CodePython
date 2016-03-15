print "** Loan Calculater **"
amount=float(raw_input("Enter Loan Amount :"))
rate=float(raw_input("Enter Interest rate :"))
yr=int(raw_input("Enter Term in years :"))

interest=amount*(rate/100)*yr
months=yr*12
totalAmount=amount+interest
print "Amount borrowed : $",amount
print "Total Amount: $",totalAmount
print "Total interest paid : $",interest
mInstallment=round((totalAmount/months),2)
print "Monthly installment = $",mInstallment

print "Pymt#    Amount paid    Remaning Balance"
print "-----    -----------    ----------------  "
pymt=0

while totalAmount>=0:
    print pymt,"        ",mInstallment,"        ",totalAmount
    totalAmount=totalAmount-mInstallment
    pymt=pymt+1
    if pymt==months:
        mInstallment==totalAmount
