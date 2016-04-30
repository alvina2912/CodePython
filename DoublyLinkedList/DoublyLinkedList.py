class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None
        self.prevousNode=None

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.nextNode=b
b.prevousNode=a
b.nextNode=c
c.prevousNode=b
c.nextNode=d
d.prevousNode=c

print a.value
print b.value
print c.value
print d.value
print a.nextNode.value
print b.nextNode.value
print b.prevousNode.value
print c.prevousNode.value
