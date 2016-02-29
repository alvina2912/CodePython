num_of_stud = int(raw_input("Enter Number of student :"))
students_data={}
for i in range (num_of_stud):
	name=raw_input("Enter Name :")
	mark1= int(raw_input("Enter marks in maths:") )
	mark2=int(raw_input("Enter marks in physics:"))
	mark3=int(raw_input("Enter marks in chemistry:"))
	students_data[name] = [mark1,mark2,mark3]
data = ""	
for n in students_data:
	 #print n, ' '.join(map(str , students_data[n]))
	 data = n 
	 for m in students_data[n]:
	 	data += " " + str(m)
	 print data

name_=raw_input("Enter student name to find average ")
sum=0
for n in students_data:
	if name_==students_data.keys():
		sum=sum+students_data[n]
ave=sum/3
print ave		
		
	 
	 
	



