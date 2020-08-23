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

def reverse_string(input_str):
    stk = Stack()

    for ch in input_str:
        stk.push(ch)

    rstr = ''
    while stk.size()!=0:
        rstr += stk.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am learning python"))