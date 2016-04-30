class Car(object):
    def __init__(self,name):
        self.name=name
        self.color="Red"
    def printName(self):
        print self.name

class Honda(Car):
    def __init__(self,nm,year):
        super(Honda,self).__init__(nm)
        self.yr=ModelYear(year)

class ModelYear:
    def __init__(self,year):
        self.y=year

h=Honda("Accord", "2008")
h.printName()
print h.yr.y
