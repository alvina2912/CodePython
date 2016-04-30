class Base(object):
    def __init__(self):
        self.s= "Base Created"
class Child(Base):
    def __init__(self):
        super(Child,self).__init__()
c=Child()
print c.s
