class Stack(object):
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1
    
    def isempty(self):
        return self.top == -1

    def isfull(self):
        return self.top + 1 == self.size

    def get_top(self):
        if self.isempty():
            raise IndexError("stack is empty!")
        else:
            return self.stack[len(self.stack - 1)]

    def push(self, x):
        if self.isfull():
            raise IndexError("stack overflow!")
        else:
            self.stack.append(x)
            self.top -= 1

    def pop(self, x):
        if self.isempty():
            raise IndexError("stack underflow")
        else:
            self.top += 1
            return self.stack.pop()





