# https://leetcode.com/problems/reverse-string/

def reverse_stack(arr):

    if len(arr) == 1 :
        return

    # pop the top element of stack and call reverse stack function of revised set
    temp = arr.pop()
    reverse_stack(arr)
    # once other stack is revised , push the previously opped element back into stack
    insert_stk(arr,temp)
    return

def insert_stk(arr,temp):

    # insert element into stack only when stack is empty
    if len(arr) == 0:
        arr.append(temp)
        return

    # if stack is not empty, pop the top element of stack and call insert function on remaing element of stack
    tmp = arr.pop()
    insert_stk(arr,temp)
    # push the previously element into stack
    arr.append(tmp)


def main():

    global arr
    arr = [4,1,6,0,2,7,3]
    reverse_stack(arr)
    print("Stack post deletion of middle element is ", arr )



if __name__ == "__main__":
    main()
