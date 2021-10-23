# https://www.geeksforgeeks.org/delete-middle-element-stack/


def del_mid_element_Stack(stk : list[int], mid : int):

    if len(stk) < 2 :
        return stk

    # if middle element position is achieved , Pop the middle element and return the function
    if mid == 1 :
        stk.pop()
        return

    temp = stk.pop() # pop an element from Stack
    del_mid_element_Stack(stk,mid-1) # Reduce the stack size and due to which middle element position will be reduced by 1 as well.
    stk.append(temp) # once middle element is deleted, push the previously popped element.

    return(stk) # return the stack in the end

def main():


    arr = [4,1,6,0,2,7,3]
    # k = ( len(arr) / 2 ) + 1  # finding middle element
    k = ( len(arr) // 2 ) + 1
    print("Stack post deletion of middle element is ", del_mid_element_Stack(arr,k))



if __name__ == "__main__":
    main()