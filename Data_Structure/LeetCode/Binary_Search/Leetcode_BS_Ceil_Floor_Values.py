#https://www.geeksforgeeks.org/floor-in-a-sorted-array/

# Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x.
# Assume than the array is sorted in Ascending order.

def BS_Floor_Soreted_Array(arr,x,start,end):

    result = -1

    while end >= start :

        mid_element = ( start + end ) //2
        if arr[mid_element] == x:
            return arr[mid_element]
        elif arr[mid_element] > x:
            ## If and element is greater than X , means it can be a possible floor value, store it
            end = mid_element-1
            result = arr[mid_element]
        elif arr[mid_element] < x:
            start = mid_element+1


    return result

# https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

def BS_Ceil_Soreted_Array(arr,x,start,end):

    result = -1

    while end >= start :

        mid_element = ( start + end ) //2
        if arr[mid_element] == x:
            return arr[mid_element]
        elif arr[mid_element] > x:
            end = mid_element-1
        elif arr[mid_element] < x:
            start = mid_element+1
            ## If and element is smaller than X , means it can be a possible ceil value, store it
            result = arr[mid_element]

    return result

#Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x,
# Assume than the array is sorted in Ascending order.


def main():
    # Driver Code
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 3

    Ceil = BS_Ceil_Soreted_Array(arr,x,0,len(arr)-1)
    Floor = BS_Floor_Soreted_Array(arr, x, 0, len(arr) - 1)

    print("Ceil Element  :" , Ceil)
    print("Floor Element :", Floor)

if __name__ == "__main__":

    main()