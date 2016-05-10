class stack(object)
    def __init__(self):
        self.items= []
        self.minStack = []
    def push(n):
        if self.minStack == []:
            self.minStack.append(n)
        elif self.minStack[len(self.minStack) - 1] > n:
            self.minStack.append(n)
        self.items.append(n)
    def pop():
        item = self.items.pop()
        if self.minStack[len(self.minStack) - 1] == item:
            self.minStack.pop()
        return item
    def min():
        if self.minStack==[]
            return
        else:
            return self.minStack[len(self.minStack) - 1]

s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(0)
s.min() #0
s.pop() #
s.min() #1
s.push(-1)
s.
