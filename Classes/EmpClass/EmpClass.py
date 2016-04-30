class EmpClass(object):
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        EmpClass.empCount+=1

    def displayCount(self):
        print "Total Emplyees are %d " %EmpClass.empCount

    def displayEmp(self):
        print "Name %s , salary %d"%(self.name,self.salary)

e1=EmpClass("Alvina",100)

e2=EmpClass("Roger",200)
e3=EmpClass("Angie",300)
e1.displayEmp()
e2.displayEmp()
e3.displayEmp()
e1.displayCount()
