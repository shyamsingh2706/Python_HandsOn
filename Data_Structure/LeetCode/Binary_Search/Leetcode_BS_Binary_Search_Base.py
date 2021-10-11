

def Binary_Search_Recurssion(arr,x,start,end):

    ## Find Middle Element of Sorted array

    if end >= start:

        Mid_element = (start + end) // 2

        if arr[Mid_element] == x :

            return Mid_element

        # Else the element can only be present
        # in right subarray , Mid+1 to end
        elif arr[Mid_element] < x :

            return Binary_Search(arr, x, Mid_element+1,end )

        # If element is smaller than mid, then it
        # can only be present in left subarray i.e. 0 to Mid-1
        elif arr[Mid_element] > x :

            return Binary_Search(arr, x, start , Mid_element-1 )

    else:

        return -1

def Binary_Search_iterative(arr,x,start,end):

    ## Find Middle Element of Sorted array

    while end >= start :

        Mid_element = (start + end) // 2

        if arr[Mid_element] == x :

            return Mid_element

        # Else the element can only be present
        # in right subarray , Mid+1 to end
        elif arr[Mid_element] < x :

            start = Mid_element+1

        # If element is smaller than mid, then it
        # can only be present in left subarray i.e. 0 to Mid-1
        elif arr[Mid_element] > x :

            end = Mid_element-1

    return -1

def main():
    # Driver Code
    arr = [2, 3, 4, 10, 40]
    x = 40

    index = Binary_Search_iterative(arr,x,0,len(arr)-1)

    print(index)

    if index != -1:
        print("Element is present at index :" , index)
    else:
        print("Element is not present in array")

if __name__ == "__main__":

    main()