# https://www.geeksforgeeks.org/next-greater-element/

# Given an array, print the Next Greater Element (NGE) for every element.
# The Next greater Element for an element x is the first greater element on the right side of x in the array.
# Elements for which no greater element exist, consider the next greater element as -1.

from collections import deque

def Stack_NGR(arr):

    stk = deque()
    NGR =[]
    for i in range(len(arr)-1,-1,-1 ):

        # if stack is empty , consider the next greater element as -1
        if len(stk) == 0:
            NGR.append(-1)
        # if stack is not empty and top element is greater than current element
        # consider Top element as next greater element
        elif len(stk) > 0 and arr[i] < stk[-1] :
            NGR.append(stk[-1])

        # if stack is not empty and top element is less than current element
        # pop until its greater than current element
        # if stack is empty i.e. no element is greater than current element. consider -1
        # else pick top element as greater element
        elif len(stk) > 0 and arr[i] > stk[-1] :
            while len(stk) > 0 and arr[i] > stk[-1]:
                stk.pop()

            if len(stk) == 0 :
                NGR.append(-1)
            else:
                NGR.append(stk[-1])

        # push current element in the stack in the end whats read
        stk.append(arr[i])

    return (NGR[::-1])


def main() :

    arr = [1,3,2,4]
    nxt_greater_element  = Stack_NGR(arr)
    print ( "Next greater Number is : ", nxt_greater_element)
if __name__ == "__main__":
    main()