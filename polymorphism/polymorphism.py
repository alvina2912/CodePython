class addition:

    def add(self):
        raise NotImplementedError("Subclass must implement abstract method")

class add2Nums(addition):
    def add(self,num1,num2):
        return self.num1+self.num2


class add3Nums(addition):
    def add(self,num1,num2,num3):
        return self.num1+self.num2+self.num3




a=add2Nums()
a1=add3Nums()
print a.add(1,2)
print a1.add(1,2,3)
