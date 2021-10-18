# https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
import ctypes.wintypes
import os
from collections import deque
import sys

class special_stack():

    def __init__(self):
        self.arr = deque()
        self.temp_arr = deque()

    ## Push Element into Secondary Stack as well if latest pushed element is less current min
    def push(self,data):

        self.arr.append(data)

        if len (self.temp_arr) == 0:
            self.temp_arr.append(data)

        elif data <= self.temp_arr[-1]:
            self.temp_arr.append(data)


    def pop(self):

        if len(self.arr) == 0:
            return "Invalid Operation,Stack empty, cant be poped"

        temp = self.arr.pop()

        ## Pop Element from Secondary Stack as well if latest Pop element is current min
        if temp == self.temp_arr[-1]:
            temp_min = self.temp_arr.pop()

        return temp

    def get_min(self):

        if len(self.temp_arr) == 0:
            return "Invalid Operation,Stack empty, cant give Minimum"
        else:
            return self.temp_arr[-1]

class special_stack_Optimized_space():

    def __init__(self):
        self.arr = deque()
        self.min = sys.maxsize

    ## Push Element into Secondary Stack as well if latest pushed element is less current min
    def push(self,data):

        if data <= self.min:

            self.arr.append(2*data-self.min)
            self.min = data

        else:
            self.arr.append(data)


    def pop(self):

        if len(self.arr) == 0:
            return "Invalid Operation,Stack empty, cant be poped"

        temp = self.arr.pop()

        ## Pop Element from Secondary Stack as well if latest Pop element is current min
        if (temp < self.min ):
            self.min = 2*self.min-temp

        return temp

    def get_min(self):

        return self.min


def main() :

    S = special_stack_Optimized_space()
    print(S.pop())

    S.push(20)
    print(S.get_min())
    S.push(10)
    S.push(30)
    S.push(40)
    print(S.get_min())
    S.push(5)
    print(S.get_min())
    S.pop()
    print(S.get_min())
    S.pop()
    S.pop()
    print(S.get_min())
    S.pop()
    print(S.get_min())

if __name__ == "__main__":
    main()