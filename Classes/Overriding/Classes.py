from Base import BaseClass

class InheritiingClass(BaseClass):
    def __init__(self):
        self.x=17

class InheritiingClass2(BaseClass):
    def printHam(self):
        print "Ham2"

class InheritiingClass3(InheritiingClass,InheritiingClass2):
    def __init__(self):
        super(InheritiingClass3,self).__init__()

print BaseClass.__subclasses__()
I=InheritiingClass3()
print I.x
I.printHam()
