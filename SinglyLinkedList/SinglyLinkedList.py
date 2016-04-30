class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.nextNode=b
b.nextNode=c
c.nextNode=d
print a.value
print b.value
print c.value
print d.value
print a.nextNode.value
print b.nextNode.value
