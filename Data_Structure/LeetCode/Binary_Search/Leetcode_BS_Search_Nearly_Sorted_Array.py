#https://www.geeksforgeeks.org/search-almost-sorted-array/

# Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions,
# i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array.
# Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].


def BS_Nearly_Sorted_Array(arr,x,start,end):

    arr_len = (len(arr) - 1)

    while end >= start :

        mid_element = (start + end ) // 2

        if arr[mid_element] == x :
            return mid_element

        if mid_element+1 <= arr_len :
            if arr[mid_element+1] == x:
                return mid_element+1

        if mid_element-1 >= 0:
            if arr[mid_element-1] == x:
                return mid_element-1

        if arr[mid_element] > x :
            end = mid_element-2
        elif arr[mid_element] < x :
            start = mid_element+2

    return -1


def main():
    # Driver Code
    arr = [10, 3, 40, 20, 50, 80, 70]
    x = 80
    Index_pos = BS_Nearly_Sorted_Array(arr,x,0,len(arr)-1)
    print(" Element's Index Postion in Nearly Sorted array is :", Index_pos)

if __name__ == "__main__":

    main()