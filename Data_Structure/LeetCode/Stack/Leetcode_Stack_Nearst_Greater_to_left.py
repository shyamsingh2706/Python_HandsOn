from collections import deque

def Stack_NGR(arr):

    stk = deque()
    NGR =[]
    for i in range(0,len(arr),1 ):


        if len(stk) == 0:
            NGR.append(-1)

        elif len(stk) > 0 and arr[i] < stk[-1] :
            NGR.append(stk[-1])

        elif len(stk) > 0 and arr[i] > stk[-1] :
            while len(stk) > 0 and arr[i] > stk[-1]:
                stk.pop()

            if len(stk) == 0 :
                NGR.append(-1)
            else:
                NGR.append(stk[-1])


        stk.append(arr[i])

    return (NGR)


def main() :

    arr = [1,3,2,4]
    nxt_greater_element_left = Stack_NGR(arr)
    print ( "Next greater Number is : ", nxt_greater_element_left)
if __name__ == "__main__":
    main()