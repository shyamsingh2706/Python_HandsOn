from collections import deque

# Build Stack Class
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# Build Queue Class
class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

#Insert element into stack ( LIFO )

stk = Stack()
stk.push(11)
stk.push(12)
stk.push(13)
stk.push(14)

print(f"Last element of stack is {stk.peek()}")
print(f"Size of stack is {stk.size()}")
print(f"Remove element of stack  {stk.pop()}")
print(f"Remove element of stack  {stk.pop()}")
print(f"Empty check on Stack :  {stk.is_empty()}")


# Build Queue in Python ( FIFO )
#Insert element into Queue

Q = Queue()
Q.enqueue(11)
Q.enqueue(12)
Q.enqueue(13)
Q.enqueue(14)

print(f"Size of Queue is {Q.size()}")
print(f"Remove element of Queue  {Q.dequeue()}")
print(f"Remove element of Queue  {Q.dequeue()}")
print(f"Empty check on Queue :  {Q.is_empty()}")