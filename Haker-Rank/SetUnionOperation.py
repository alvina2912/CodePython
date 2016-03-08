n=raw_input("Enter the number of students who have subscribed to the English newspaper : ")
rollNumbersEnglish=set(raw_input("Enter Roll numbers : ").split())
m=raw_input("Enter the number of students who have subscribed to the French newspaper : ")
rollNumbersFrench=set(raw_input("Enter Roll numbers : ").split())
print "English Roll Numbers :",rollNumbersEnglish
print "French Roll Numbers :",rollNumbersFrench
print "Number of students reading at least one newspaper :",len(rollNumbersEnglish.union(rollNumbersFrench)  )

print "Number of students reading both newspaper :"",len(rollNumbersEnglish.intersection(rollNumbersFrench)  )
print "Number of students reading only English newspaper :",len(rollNumbersEnglish.difference(rollNumbersFrench)  )
print "Number of students reading either English or French newspaper but not both :",len(rollNumbersEnglish.symmetric_difference(rollNumbersFrench)  )
