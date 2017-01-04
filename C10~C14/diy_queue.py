from collections import deque
class Queue():
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = -1
        self.queue = deque()

    def isfull(self):
        return self.tail - self.head + 1 == self.size

    def isempty(self):
        return self.head == self.tail

    def enqueue(self, x):
        if self.isfull():
            raise IndexError("queue is full!")
        else:
            self.queue.append(x)
            self.tail = self.tail +1

    def dequeue(self):
        if self.isempty():
            raise IndexError("queue is empty!")
        else:
            self.head = self.head + 1
            return self.queue.popleft()


