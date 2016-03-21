#The National University conducts an examination of NN students in XX subjects.
#Your task is to compute the average scores of each student.

n= int(raw_input("Enter Number of Student : "))
x= int(raw_input("Enter number of subjetcs : "))
sub1=[int(raw_input("Enter marks for subject 1 for  :")) for i in range(x)]
sub2=[int(raw_input("Enter marks for subject 2 for  :")) for i in range(x)]
sub3=[int(raw_input("Enter marks for subject 3 for  :")) for i in range(x)]
print "sub1 : ",sub1
print "sub2 : ",sub2
print "sun3 : ",sub3

marks=zip(sub1,sub2,sub3)
print marks

result =map(sum, marks)
print result
for i in range(len(result)):
    avg=result[i]/x
    print avg
