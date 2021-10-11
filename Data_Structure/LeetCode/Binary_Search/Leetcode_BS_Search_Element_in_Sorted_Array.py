# https://leetcode.com/problems/search-in-rotated-sorted-array/

def Root_Index_In_Rotated_Sorted_Array(arr):

    N = len(arr)
    start = 0
    end = N-1

    while end >= start:

        mid_element = (start+end) // 2
        next_element = (mid_element+1) % N
        prev_element = (mid_element+N-1) % N

        if arr[mid_element] < arr[next_element] and arr[mid_element] < arr[prev_element]:
            return mid_element
        else:
            if arr[mid_element]>=arr[start] and arr[mid_element]<=arr[end]:
                return start
            elif arr[mid_element] >= arr[start]:
                start = mid_element+1
            elif arr[mid_element] <= arr[end]:
                end = mid_element-1

def Binary_search(arr,x,start,end):

    while end >= start:

        mid_element = (start + end ) // 2
        if arr[mid_element] == x:
            return mid_element
        elif arr[mid_element] > x:
            end = mid_element-1
        elif arr[mid_element] < x :
            start = mid_element+1

    return -1

def main():
    # Driver Code
    arr = [4,5,6,7,0,1,2]
    x = 2
    root_index_pos = Root_Index_In_Rotated_Sorted_Array(arr )
    print("Root Index Postion in Sorted array is :", root_index_pos)

    left_Arr_BS = Binary_search(arr,x,0,root_index_pos-1)
    right_Arr_BS = Binary_search(arr, x, root_index_pos, len(arr) -1)

    if left_Arr_BS != -1 :
        print("Index Postion in the element is :", left_Arr_BS)
    elif right_Arr_BS != -1 :
        print("Index Postion in the element is :", right_Arr_BS)
    else:
        print("Element not found !")

if __name__ == "__main__":

    main()