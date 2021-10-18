from collections import deque

def Stack_NGR(arr):

    stk = deque()
    NGR =[]
    for i in range(len(arr)-1,-1,-1 ):


        if len(stk) == 0:
            NGR.append(-1)

        elif len(stk) > 0 and arr[i] > stk[-1] :
            NGR.append(stk[-1])


        elif len(stk) > 0 and arr[i] < stk[-1] :
            while len(stk) > 0 and arr[i] < stk[-1]:
                stk.pop()

            if len(stk) == 0 :
                NGR.append(-1)
            else:
                NGR.append(stk[-1])


        stk.append(arr[i])

    return (NGR[::-1])


def main() :

    arr = [4,5,2,10,8]
    nxt_smaller_element_R  = Stack_NGR(arr)
    print ( "Nearest Smaller Number to Right is : ", nxt_smaller_element_R)
if __name__ == "__main__":
    main()